# Nhập vào điểm trung bình, in ra loại học lực

x = input('Điểm trung bình: ')
x = float(x)

if x < 5.0:
    print('Học lực kém')
elif x < 6.5:
    print('Học lực trung bình')
elif x < 8.0:
    print('Học lực khá')
else:
    print('Học lực giỏi')

