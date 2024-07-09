import time
import multiprocessing
def cal_sq(num):
    print("sq nnumbers:")
    for n in num:
        time.sleep(0.2)
        print('Square:',n*n)
def cal_cu(num):
    print("cube nnumbers:")
    for n in num:
        time.sleep(0.2)
        print('cube:',n*n*n)
if __name__=="__main__":
    a=[1,2,3,4]
    p1=multiprocessing.Process(target=cal_sq,args=(a,))
    p2=multiprocessing.Process(target=cal_cu,args=(a,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
