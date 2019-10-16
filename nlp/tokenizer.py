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
    sentence = sentence.lower()
    words = ViTokenizer.tokenize(sentence).split()
    words = [word for word in words if normalize(word).isalpha()]
    return words

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
