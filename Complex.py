class Complex:

    def __init__(self, real1, img1, real2, img2):
        self.real1 = real1
        self.img1 = img1
        self.real2 = real2
        self.img2 = img2

    def __add__(self):
        return (self.real1 + self.real2) , " + i", (self.img1 + self.img2) 
    
real1 = int(input("Enter real part of 1 : "))
img1 = int(input("Enter imaginary part of 1 : "))
real2 = int(input("Enter real part of 2 : "))
img2 = int(input("Enter imaginary part of 1 : "))

c1 = Complex(real1, img1, real2, img2)
c1.__add__()