"""
Chương trình in ra các số nguyên tố nhỏ hơn 1000
"""

ds = []

for x in range(2, 1000):
    nt = True

    for p in ds:
        if x % p == 0:
             nt = False
             break

        if p *p > x:
             break    

    if nt:
        ds.append(x)

print(ds)
