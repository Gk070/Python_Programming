a = int(input("Enter number1 : "))
b = int(input("Enter number2 : "))

def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)

gcd(a, b)