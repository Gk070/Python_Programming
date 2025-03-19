class Base1:
    
    def Func1(self):
        print("Function 1")
    
class Derived1(Base1):

    def Func2(self):
        print("Function 2")

class Derived2(Derived1):

    def Func3(self):
        print("Function 3")

d2 = Derived2()
d2.Func2()
d2.Func3()
d2.Func1()