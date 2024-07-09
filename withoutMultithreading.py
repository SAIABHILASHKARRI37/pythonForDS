import time
def cal_sq(num):
    print("sq nnumbers:")
    l=[n*n for n in num]
    time.sleep(0.2)
    print('Square:',l)
def cal_cu(num):
    print("cu nnumbers:")
    l=[n*n*n for n in num]
    time.sleep(0.2)
    print('Cube:',l)
a=[1,2,3,4]
t=time.time()
cal_sq(a)
cal_cu(a)
print('time taken is:',time.time()-t)