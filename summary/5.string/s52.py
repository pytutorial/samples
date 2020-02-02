#Nhập vào họ tên đầy đủ một người. In ra họ, tên đệm, tên

hoten = input('Họ và tên: ')
items = hoten.split()

ho = items[0]
tendem = ' '.join(items[1:-1])
ten = items[-1]

print('Họ: ', ho)
print('Tên đệm: ', tendem)
print('Tên: ', ten)