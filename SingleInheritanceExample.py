class Base:

    def func1(self):
        print("Function 1")

class Derived(Base):

    def func2(self):
        print("Function 2")

d = Derived()
d.func1()
d.func2()