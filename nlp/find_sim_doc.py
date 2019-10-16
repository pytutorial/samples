import json
from tokenizer import tokenize

text = '''Từ 15h00 chiều nay (16/10), giá xăng E5RON92 được điều chỉnh giảm 310 đồng/lít; 
Xăng RON95-III giảm 271 đồng/lít, dầu mazut giảm mạnh nhất với 2.103 đồng/kg.'''

text_words = set(tokenize(text))

topics = ['xahoi' , 'kinhdoanh', 'thethao', 'vanhoa']
docs = []

with open('docs.json') as f:
    docs = json.load(f)

scores = []

for i, doc in enumerate(docs):
    doc_words = set(doc['words'])
    intersect_words = doc_words.intersection(text_words)
    union_words = doc_words.union(text_words)
    score = len(intersect_words)/len(union_words)
    scores.append((score, i))
    
scores = sorted(scores, reverse=True)

for _, i in scores[:5]:
    print(docs[i]['sentence'])
        
        
        
        
