"""
Chương trình tìm 2 số khi biết tổng và tỉ số
 - Đầu vào :
   + S : tổng của 2 số
   + R : thương của 2 số
 - Đầu ra:
   + Giá trị 2 số
"""

S = input('S = ')
S = float(S)

R = input('R = ')
R = float(R)

a = S / (1+R)
b = a * R

print('a = ', a)
print('b = ', b)
