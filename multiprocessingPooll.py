import multiprocessing
def f(n):
    return n*n
if __name__=='__main__':
    l=[1,2,3,4]
    p=multiprocessing.Pool()
    r=p.map(f, l)
    p.close()
    p.join()
    print(r)


