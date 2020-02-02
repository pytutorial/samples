# Cho trước dãy số, nhập vào một số. Kiểm tra số có nằm trong dãy số hay không. Nếu có thì xóa số đó khỏi dãy số.

lst = [1, 2, 3, 4, 5, 7, 9, 11, 12, 14]

x = input("x=")
x = int(x)

if x in lst:
    lst.remove(x)
    print('Dãy số mới: ', lst)
else:
    print(x, 'không nằm trong dãy số')