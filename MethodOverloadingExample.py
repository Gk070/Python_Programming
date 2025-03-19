class Area:

    def find_Area(self, a = None, b = None):

        if a != None and b != None:
            print("Area of rectangle is : ", a * b)
        elif a != None:
            print("Area of square is : ", a * a)
        else:
            print("No figure assigned")

ob1 = Area()
ob1.find_Area()
ob1.find_Area(2)
ob1.find_Area(4, 5)