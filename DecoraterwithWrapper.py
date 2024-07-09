import time
def time_it(func):
    def wrapper(*arg,**karg):
        start=time.perf_counter()
        result=func(*arg,**karg)
        end=time.perf_counter()
        print("time is:"+func.__name__ +str((end-start)*1000)+'milli sec')
        return result
    return wrapper
@time_it
def cal_sq(num):
   
    result=[]
    for n in num:
        result.append(n*n)
    return result
@time_it
def cal_cube(num):
    
    result=[]
    for n in num:
        result.append(n*n*n)
    
    return result
num=range(1,10)
r1=cal_sq(num)
r2=cal_cube(num)
#pref_counter()-this gives us accurate time for small time executions than time()
        