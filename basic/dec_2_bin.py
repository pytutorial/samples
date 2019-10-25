"""
Chương trình chuyển một số từ hệ thập phân sang nhị phân
"""

x = 2000
s = ''

while x > 0:
    i = x % 2
    s = str(i) + s
    x = int(x/2)

print(s)


