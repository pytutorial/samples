"""
Chương trình tính diện tích tam giác trên mặt phẳng
 - Đầu vào : tọa độ 3 đỉnh tam giác
 - Đầu ra : diện tích tam giác
"""

x1, y1 = 1, 1
x2, y2 = 2, 3
x3, y3 = 0, 0

X1 = x1 - x3
Y1 = y1 - y3

X2 = x2 - x3
Y2 = y2 - y3

S0 = X1 * Y2
S1 = 0.5 * X1 * Y1
S2 = 0.5 * X2 * Y2
S3 = 0.5 * (X1-X2)*(Y2-Y1)
S = abs(S0 - S1 - S2 -S3)

print('Diện tích tam giác : ', round(S, 6))

