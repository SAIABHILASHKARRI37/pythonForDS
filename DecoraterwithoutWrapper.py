import time
def cal_sq(num):
    start=time.perf_counter()
    result=[]
    for n in num:
        result.append(n*n)
    end=time.perf_counter()
    print('time taken to ex is'+str((end-start)*1000)+"mil sec")
    return result
def cal_cube(num):
    start=time.perf_counter()
    result=[]
    for n in num:
        result.append(n*n*n)
    end=time.perf_counter()
    print('time taken to ex is'+str((end-start)*1000)+"mil sec")
    return result
num=range(1,10)
r1=cal_sq(num)
r2=cal_cube(num)
#pref_counter()-this gives us accurate time for small time executions than time()
        