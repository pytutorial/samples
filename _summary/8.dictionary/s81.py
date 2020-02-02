# Cho một từ điển. In ra nghĩa của từng từ trong từ điển. Nhập vào một từ, in ra nghĩa của từ đó nếu có, nếu từ không nằm trong từ điển thì in ra "Không tồn tại"

d = {'one': 'một', 'two': 'hai', 'three': 'ba'}
d['four'] = 'bốn'
d.update({'five': 'năm', 'six': 'sáu'})

for k,v in d.items():
    print(k, ':', v)
    
word = input('Nhập từ cần tra nghĩa: ')

if word in d:
    print(d[word])
else:
    print('Không tồn tại')
    
print(d.get(word, 'Không tồn tại')) # cách 2