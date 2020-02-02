# Nhập vào họ, tên đệm, tên của một người. In ra tên đầy đủ

ho = input('Họ: ')
tendem = input('Tên đệm: ')
ten = input('Tên: ')

hoten = ho + ' ' + tendem + ' ' + ten
hoten = f'{ho} {tendem} {ten}'   #cách 2

print("Họ và tên: ", hoten)