import json
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
from random import shuffle

with open('docs.json') as f:
    docs = json.load(f)

shuffle(docs)
docs = docs[:5000]

word_count = {}
for doc in docs:
    for word in doc['words']:
        word_count[word] = 1 + word_count.get(word, 0)
            
word_items = sorted(word_count.items(), key=lambda x : x[1], reverse=True)
n_word = 5000

wordlist = []
for word, count in word_count.items():
    if count <= len(docs)/2:
        wordlist.append(word)
        if len(wordlist) == n_word:
            break

with open('wordlist.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(wordlist))    
    
word_indexes = {word : i for (i, word) in enumerate(wordlist)}

def doc_to_vec(doc):
    vec = [0] * n_word
    for word in doc['words']:
        index = word_indexes.get(word, -1)
        if index >= 0:
            vec[index] = 1
    return vec

X = []
y = []
for doc in docs:
    X.append(doc_to_vec(doc))
    y.append(doc['category'])

Ntrain = 4000
Xtrain, ytrain = X[:Ntrain], y[:Ntrain]
Xtest, ytest = X[Ntrain:], y[Ntrain:]

model = MLPClassifier(hidden_layer_sizes=(10,), verbose=True)
model.fit(Xtrain, ytrain)

print('Accuracy : ', model.score(Xtest, ytest))
joblib.dump(model, 'model.bin')