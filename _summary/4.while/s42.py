# Cho trước số N, tính số chữ số của N trong hệ nhị phân (số bit biểu diễn N)

N = input('N=')
N = int(N) 

digits = 0
while N > 0:
    digits += 1
    N //= 2
    
print('Số bit biểu diễn N:', digits)