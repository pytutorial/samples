# Cho trước số N, tìm số K nhỏ nhất để 1+2+...+K > N

N = input('N=')
N = int(N)

K = 0
S = 0

while S <= N:
    K += 1
    S += K

print('K=', K)