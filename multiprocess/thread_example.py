from threading import Thread

a = []

def func(threadId):
    a.append(threadId)
    print(f'Inside thread {threadId} : a = ', a)
   
for i in range(5):
   thr = Thread(target=func, args=(i,))
   thr.start()