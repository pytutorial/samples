from tokenizer import tokenize
from sklearn.externals import joblib

topics = ['Xã hội' , 'Kinh doanh', 'Thể thao', 'Văn hóa']

model = joblib.load('model.bin')

with open('wordlist.txt', encoding='utf-8') as f:
    wordlist = [line.strip() for line in f]

n_word = len(wordlist)
word_indexes = {word : i for (i, word) in enumerate(wordlist)}

text = '''Thực hiện thí điểm việc không tổ chức hội đồng nhân dân phường tại Hà Nội 
trong nhiệm kỳ 2021 – 2026, Chính phủ đề xuất bổ sung 2 thẩm quyền cho 
Chủ tịch UBND quận, một trong số đó là quyền cách chức người đứng đầu 
cơ quan hành chính cấp dưới.'''
    
tokens = tokenize(text)
x = [0] * n_word

for word in tokens:
    index = word_indexes.get(word, -1)
    if index >= 0:
        x[index] = 1
        
category = model.predict([x])[0]
print(topics[category])        
        