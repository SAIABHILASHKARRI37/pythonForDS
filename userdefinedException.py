#Exceptions are instances of class
class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def print(self):
        print('user defined exception',self.msg)
try:
    raise Accident("cars crashed")
except Accident as e:
    e.print()
finally:
    print('user defined exception learned')