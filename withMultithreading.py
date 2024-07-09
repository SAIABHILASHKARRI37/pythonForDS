import time 
import threading
def cal_sq(num):
    print("sq nnumbers:")
    for n in num:
        time.sleep(0.2)
        print('Square:',n*n)  
def cal_cu(num):
    print("cu nnumbers:")
    for n in num:
        time.sleep(0.2)
        print('Cube:',n*n*n) 
a=[1,2,3,4]
t=time.time()
t1=threading.Thread(target=cal_sq,args=(a,))
t2=threading.Thread(target=cal_cu,args=(a,))
t1.start()
t2.start()
t1.join()
t2.join()

print('time taken is:',time.time()-t)