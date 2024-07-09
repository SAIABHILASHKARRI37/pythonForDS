#fibonacci using generator
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for d in fib():
    if d>50 :
        break
    print(d)