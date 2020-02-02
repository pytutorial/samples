#Tạo một file văn bản và ghi vào file một số dòng

f = open('test.txt', 'w', encoding='utf-8')
f.write('Xin chào\n')
f.write('Bạn có khỏe không?')
f.close()