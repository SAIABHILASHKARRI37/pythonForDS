import time
import multiprocessing


def deposit(amount,l):
    for i in range(1,10):
        l.acquire()
        time.sleep(0.1)
        amount.value=amount.value+1
        l.release()

def withdraw(amount,l):
    for i in range(1,10):
        l.acquire()
        time.sleep(0.2)
        amount.value=amount.value-1
        l.release()

if __name__=="__main__":
    balence=multiprocessing.Value('i',200)
    lock=multiprocessing.Lock()
    d=multiprocessing.Process(target=deposit,args=(balence,lock))
    w=multiprocessing.Process(target=withdraw,args=(balence,lock))
    d.start()
    w.start()
    
    d.join()
    w.join()
    print(balence.value)