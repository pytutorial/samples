"""
Chương trình mã hóa bức điện
 - Đầu vào :
   + Khóa k (0 <= k <= 25) dùng để mã hóa
   + Bức điện cần mã hóa
 - Đầu ra:
   + Bức điện được mã hóa, trong đó mỗi kí tự được dịch đi k vị trí trong bảng chữ cái tiếng Anh
"""

k = 10
msg = 'TOI NAY CO DI CHOI KHONG'

enc_msg = ''
for c in msg:
    if c == ' ':
        enc_msg += c
    else:
        x = ord(c) - ord('A')
        x += k
        x = x % 26
        x = x + ord('A')
        enc_msg += chr(x)

print(enc_msg)
