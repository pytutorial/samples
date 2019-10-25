"""
Chương trình tính khoảng cách 2 điểm trong mặt phẳng
 - Đầu vào :
   + (x1, y1) : tọa độ điểm thứ nhất
   + (x2, y2) : tọa độ điểm thứ hai
 - Đầu ra:
   + Khoảng cách giữa 2 điểm
"""

import math

x1, y1 = 1 , 1
x2, y2 = 4, 5

dx = x2 - x1
dy = y2 - y1

d = math.sqrt(dx*dx + dy*dy)

print('Khoảng cách giữa 2 điểm : ', round(d, 6))
 
