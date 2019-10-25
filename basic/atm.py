"""
Chương trình tính số tờ tiền trả lại của máy ATM
 - Đầu vào : Số tiền máy ATM cần trả lại (bội số của 5k)
 - Đầu ra: Số tờ của từng loại tiền 50k, 20k, 5k 
   sao cho tổng số tờ trả lại ít nhất
"""

tientralai = input('Số tiền cần trả lại (nghìn đồng) :')
tientralai = int(tientralai)

soto50k = tientralai // 50
tientralai %= 50

soto20k = tientralai // 20
tientralai %= 20

soto5k = tientralai // 5

print('Số tờ tiền 50k : ', soto50k)
print('Số tờ tiền 20k : ', soto20k)
print('Số tờ tiền 5k : ', soto5k)
