class Father:
    def __init__(self):
        print('I am father')
    def giftf(self):
        print("gift from his father is cricket kit")
class mother:
    def __init__(self):
        print('I am mother')
    def giftm(self):
        print("gift from his mother is Books")
class Child(Father,mother):
    def __init__(self):
        print("I am child of father and mother")
    def feeling(self):
        print("i inherts sports from my father and education from my mother")
c=Child()
c.giftf()
c.giftm()
c.feeling()