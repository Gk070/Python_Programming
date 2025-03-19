class Base1:
    
    def Func1(self):
        print("Function 1")
    
class Base2:

    def Func2(self):
        print("Function 2")

class Derived(Base1, Base2):

    def Func3(self):
        print("Function 3")

d = Derived()
d.Func1()
d.Func2()
d.Func3()