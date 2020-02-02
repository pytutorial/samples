# Viết hàm tính tổng một danh sách số

def getsum(lst):
    S = 0
    for x in lst: 
        S += x
    return S
    
print(getsum([1, 3, 5, 7, 10]))