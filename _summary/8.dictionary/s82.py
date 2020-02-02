# Cho một danh sách số (có thể trùng nhau). In ra số lần xuất hiện của mỗi số trong danh sách 

lst = [1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 4]

counts = {}

for x in lst:
    counts[x] = counts.get(x, 0) + 1
    
for x in counts:
    print(x, ':', counts[x])