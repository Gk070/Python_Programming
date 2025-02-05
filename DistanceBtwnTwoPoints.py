# Program two find distance between two points
import math

x1 = int(input("Enter value of x1 : "))
y1 = int(input("Enter value of y1 : "))
x2 = int(input("Enter value of x2 : "))
y2 = int(input("Enter value of y2 : "))

d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print("Distance is : ", d)