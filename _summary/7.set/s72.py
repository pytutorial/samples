# Cho 2 danh sách số, tìm các phần tử chung nhau (phân biệt) của 2 danh sách này.

lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = [2, 3, 5, 7, 9]

s1 = set(lst1)
s2 = set(lst2)

commons = s1.intersection(s2)

print(commons)