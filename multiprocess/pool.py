from multiprocessing import Pool

def func(arr):
   return sum(arr)
   
if __name__ == '__main__':
   p = Pool(4)
   a = list(range(400))
   result = p.map(func, (a[:100], a[100:200], a[200:300], a[300:]))
   print(result)