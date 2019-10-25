"""
Chương trình tính khoảng cách giữa 2 điểm trên mặt đất theo tọa độ GPS
 - Đầu vào :
   + (kd1, vd1) : kinh độ, vĩ độ điểm thứ 1
   + (kd2, vd2) : kinh độ, vĩ độ điểm thứ 2
   + Bán kính trái đất = 6371 km
 - Đầu ra:
   + Khoảng cách (theo km) giữa 2 điểm
"""

import math

R = 6371

vd1 = 21.0259198
kd1 = 105.8444646 

vd2 = 21.0379367
kd2 = 105.8324912

vd = (vd1+vd2)/2
phi = math.pi * vd/180
R1 = R * math.cos(phi)
dx = R1 * math.pi * abs(kd2-kd1)/180
dy = R * math.pi * abs(vd2-vd1)/180

d = math.sqrt(dx*dx + dy*dy)

print('Khoảng cách giữa 2 điểm : ', round(d, 6))

