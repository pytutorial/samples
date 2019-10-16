import json
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
from random import shuffle

with open('docs.json') as f:
    docs = json.load(f)

shuffle(docs)
docs = docs[:5000]

word_count = {}
ignore_words = set()
for doc in docs:
    for word in doc['words']:
        word_count[word] = 1 + word_count.get(word, 0)

items = word_count.items()
items = [x for x in items if x[1] <= len(docs)/2]
items = sorted(items, key=lambda x : x[1], reverse=True)

wordlist = [x[0] for x in items[:5000]]
word_indexes = {word:i for (i,word) in enumerate(wordlist)}

with open('wordlist.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(wordlist))    

def doc_to_vec(doc):
    vec = [0] * len(wordlist)
    for word in doc['words']:
        index = word_indexes.get(word, -1)
        if index >= 0:
            vec[index] = 1
    return vec

X = [doc_to_vec(doc) for doc in docs]
y = [doc['category'] for doc in docs]

Xtrain, ytrain = X[:4000], y[:4000]
Xtest, ytest = X[4000:5000], y[4000:5000]

model = MLPClassifier(hidden_layer_sizes=(10,), verbose=True)
model.fit(Xtrain, ytrain)

print('Accuracy : ', model.score(Xtest, ytest))
joblib.dump(model, 'model.bin')