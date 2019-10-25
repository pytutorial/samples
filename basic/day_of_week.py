"""
Chương trình xác định thứ trong tuần của một ngày
 - Đầu vào : Ngày, tháng, năm (trong thế kỉ 21)
 - Đầu ra : Xác định ngày đó là thứ mấy
"""

day_of_week = ['thứ hai', 'thứ ba', 'thứ tư', 'thứ năm', 'thứ sáu', 'thứ bảy', 'chủ nhật']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date = int(input('Ngày : '))
month = int(input('Tháng : '))
year = int(input('Năm (trong thế kỉ 21) : '))

if date <= 0 or month <= 0 or year < 2000:
    exit()

year -= 2000
days_since_2000 = (year//4) * (365*4+1)
days_since_2000 += (year%4) * 365
   
for x in range(month-1):
    days_since_2000 += days_in_month[x]

days_since_2000 += date-1
    
if year%4 != 0 or month > 2:
    days_since_2000 += 1

dow = day_of_week[(5+days_since_2000) % 7]
print('Ngày đã nhập là ', dow)
    
