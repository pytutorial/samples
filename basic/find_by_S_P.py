"""
Chương trình tìm 2 số khi biết tổng và tích
 - Đầu vào :
   + S : tổng của 2 số
   + P : tích của 2 số
 - Đầu ra:
   + Giá trị 2 số nếu tồn tại, nếu không thông báo không tồn tại 2 số
"""

import math

S = float(input('S = '))
P = float(input('P = '))

delta = S*S - 4*P

if delta < 0:
    print('Không tồn tại 2 số thỏa mãn yêu cầu')
    exit()

sqrt_delta = math.sqrt(delta)
a = (S - sqrt_delta)/2
b = (S + sqrt_delta)/2

print('a = ', a)
print('b = ', b)
