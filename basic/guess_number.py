"""
Chương trình đoán số tự nhiên.
Bạn hãy nghĩ trong đầu một số từ 0 đến 1000
Máy tính sẽ hỏi dưới 10 câu, mỗi câu bạn chỉ trả lời Y/N xem câu đó đúng hay sai. 
Sau 10 câu hỏi, máy tính sẽ đưa ra số bạn đang nghĩ là gì.
"""

low = 0
high = 1000

print('Bạn hãy nghĩ một số trong phạm vi từ 0 đến 1000, sau đó trả lời các câu hỏi sau.')

while low + 1 != high:
    mid = (low + high) // 2
    a = input('Số đó lớn hơn ' + str(mid)  + ' ? (Y/N) : ')
    
    if a == 'Y':
        low = mid
    else:
        high = mid

print('Số bạn nghĩ là ', high)

