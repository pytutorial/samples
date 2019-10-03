from multiprocessing import Process

a = []

def func(procId):
    a.append(procId)
    print(f'Inside process {procId} : a = ', a)
   
if __name__ == '__main__':   
    for i in range(5):
       proc = Process(target=func, args=(i,))
       proc.start()   