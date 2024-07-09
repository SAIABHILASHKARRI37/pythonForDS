class cricketer:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def U_19(self):
        if self.age<19 and self.age>=14:
            print(self.name,'plays under 19 category')
        else:
            print(self.name,'dont know which category he comes due to age issues')
c=cricketer('abhi',18)
c.U_19()