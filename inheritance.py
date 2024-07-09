class A:
    def  a(self):
        print("i am a father b and c")
class B(A):
    def b(self):
        self.a()
        print('i am son of A')
x=B()

x.b()