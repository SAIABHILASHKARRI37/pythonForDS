import multiprocessing
def sq(number,q):
    for n in number:
        q.put(n*n)
if __name__=="__main__":
    number=[1,2,3]
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=sq,args=(number,q))
    p.start()
    p.join()
    while q.empty() is False:
        print(q.get())

