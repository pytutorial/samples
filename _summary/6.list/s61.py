# Cho trước dãy số, tách các số chẵn và số lẻ thành 2 dãy số mới.

lst = [1, 2, 3, 4, 5, 7, 9, 11, 12, 14]

lst_chan = []
lst_le = []

for x in lst:
    if x%2 == 0:
        lst_chan.append(x)
    else:
        lst_le.append(x)
        
print(lst_chan)
print(lst_le)