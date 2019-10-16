import os
import json
from pyvi import ViTokenizer
import unicodedata

topics = ['xahoi' , 'kinhdoanh', 'thethao', 'vanhoa']

def normalize(s):
    s = unicodedata.normalize('NFD', s)
    lst = [c for c in s if 'A' <= c.upper() <= 'Z' or c == ' ']
    return ''.join(lst)

def tokenize(sentence):
    sentence = ViTokenizer.tokenize(sentence)
    tokens = []
    for word in sentence.split():        
        if word.replace('_', '').isalpha() and len(word) > 1:
            tokens.append(word.lower())
    return tokens

if __name__ == '__main__':
    docs = []

    for i, topic in enumerate(topics):
        print('Reading topic : ', topic)
        fn = os.path.join('data', topic + '.txt')
        f = open(fn, encoding='utf-8')
        lines = f.readlines()
        f.close()
        for line in lines[:5000]:
            words = set(tokenize(line))
            words = list(words)
            docs.append({'words' : words, 'sentence': line, 'category' : i})
            
    with open('docs.json','w') as f:
        json.dump(docs, f)       
