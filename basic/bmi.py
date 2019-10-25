"""
Chương trình tính chỉ số BMI và kiểm tra thân hình
 - Đầu vào : 
    + Chiều cao (mét)
    + Cân nặng (kg)
 - Đầu ra : 
     + Chỉ số BMI = Cân nặng chia bình phương chiều cao
     + Tình trạng thân hình : Gầy/Béo/Bình thường 
"""

height = input('Chiều cao (mét) : ')
height = float(height)

mass = input('Cân nặng (kg) : ')
mass = float(mass)

bmi = mass / (height * height)

if bmi < 15:
    print('Thân hình quá gầy')

elif bmi < 16:
    print('Thân hình gầy')

elif bmi < 18.5:
    print('Thân hình hơi gầy')

elif bmi < 25:
    print('Thân hình bình thường')

elif bmi < 30:
    print('Thân hình hơi béo')

elif bmi < 35:
    print('Thân hình béo')

else:
    print('Thân hình quá béo')

