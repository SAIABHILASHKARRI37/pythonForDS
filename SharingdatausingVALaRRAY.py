import multiprocessing
def cal_sq(num,ar,v):
    v.value=12

    for idx,n in enumerate(num):#we use enum to iterate over lists.for loop lo index thelskodaniki.
        ar[idx]=n*n
if __name__=="__main__":
    a=[1,2,3]
    ar=multiprocessing.Array('i',3)
    v=multiprocessing.Value('i',0)
    p=multiprocessing.Process(target=cal_sq,args=(a,ar,v))
    p.start()
    p.join()
    print(ar[:])
    print(v.value)