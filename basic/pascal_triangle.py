"""
Chương trình in ra 10 dòng đầu của tam giác Pascal
"""

N = 10
heso = []

for i in range(N):
    heso.append(1)
    for j in range(i-1, 0, -1):
        heso[j] += heso[j-1]

    print(heso)

