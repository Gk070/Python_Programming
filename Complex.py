class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)
    
    def __str__(self):
        return f"({self.real} + {self.img}i)"
    
real1 = int(input("Enter real part of 1 : "))
img1 = int(input("Enter imaginary part of 1 : "))
real2 = int(input("Enter real part of 2 : "))
img2 = int(input("Enter imaginary part of 1 : "))

c1 = Complex(real1, img1)
c2 = Complex(real2, img2)

result = c1 + c2

print("Sum is : ", result)