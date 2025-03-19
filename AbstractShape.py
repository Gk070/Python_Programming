from abc import ABC, abstractclassmethod
import math

class Shape:

    @abstractclassmethod
    def area(self):
        pass

    def circumference(self):
        pass

class Circle(Shape):

    def area(self, r):
        print(math.pi * r * r)

    def circumference(self, r):
        print(2 * math.pi * r)

class Square(Shape):

    def area(self, s):
        print(s * s)

    def circumference(self, s):
        print(4 * s)
    
r = int(input("Enter length : "))

c1 =  Circle()
c1.area(r)
c1.circumference(r)

s1 = Square()
s1.area(r)
s1.circumference(r)