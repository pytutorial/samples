"""
Chương trình tính diện tích của một đa giác (không nhất thiết lồi) trên mặt phẳng
 - Đầu vào : danh sách toạ độ (x,y) của các đỉnh đa giác
 - Đầu ra : diện tích đa giác
"""

points = [(0,0), (1,1), (2,0), (2,-1), (1,0), (0,-1)]

area = 0

N = len(points)
x0, y0 = points[0]

for i in range(1,N-1):
	x1, y1 = points[i]
	x2, y2 = points[i+1]
	X1 = x1 - x0
	Y1 = y1 - y0
	X2 = x2 - x0
	Y2 = y2 - y0
	area += 0.5*(X1*Y2 - X2*Y1)
	
area = abs(area)

print('Diện tích đa giác : ', round(area, 6))
