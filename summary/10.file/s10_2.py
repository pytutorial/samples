# Mở 1 file và đọc từng dòng trong file

f = open('test.txt', encoding='utf-8')

for line in f:
    line = line.strip() # Bỏ kí tự \n ở cuối dòng
    print(line)
    
f.close()    