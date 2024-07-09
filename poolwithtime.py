import multiprocessing
import time
def f(n):
    sum=0
    for x in range(5):
        sum+=x
    return sum #less time it takes by using pool than normal execution
if __name__=='__main__':
    s=time.time()
    p=multiprocessing.Pool()
    r=p.map(f,range(2))
    p.close()
    p.join()
    e=time.time()
    print('time taken by pool:'+str((e-s)))

    s1=time.time()
    r=[]
    for i in range(2):
        r.append(f(i))
    
    s2=time.time()
    print('time taken by normal execution:'+str((s2-s1)))
    
    





    r=[]
    for i in range(3):
        r.append(f(i))
    print(r)