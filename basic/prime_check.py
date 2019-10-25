"""
Chương trình kiểm tra một số tự nhiên có phải là số nguyên tố không
"""

x = 8477216359

i = 2
while i * i <= x:
    if x % i == 0:
        j = x // i
        print(x, '=', i , '*', j)
        exit()
    i += 1

print(x, ' là số nguyên tố')

