"""
Chương trình kiểm tra tính hợp lệ của một ngày
 - Đầu vào : Ngày , tháng, năm (2000-2099)
 - Đầu ra : Có tồn tại ngày đó không
"""

D = int(input('Ngày: '))
M = int(input('Tháng: '))
Y = int(input('Năm (2000-2099): '))

day_in_month = 30

if M == 2:
    day_in_month = 29 if (Y%4 == 0) else 28
if (M <=7 and M%2==1) or (M >=8 and M%2==0):
    day_in_month = 31

if 1<=D<=day_in_month and 1<=M<=12:
    print('Ngày hợp lệ')
else:
    print('Ngày không hợp lệ')

