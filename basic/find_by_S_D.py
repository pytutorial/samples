"""
Chương trình tìm 2 số khi biết tổng và hiệu
 - Đầu vào :
   + S : tổng của 2 số
   + D : hiệu của 2 số
 - Đầu ra:
   + Giá trị 2 số
"""

S = input('S = ')
S = float(S)

D = input('D = ')
D = float(D)

a = (S - D)/2
b = (S + D)/2

print('a = ', a)
print('b = ', b)
