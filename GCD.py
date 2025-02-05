a = int(input("Enter number1 : "))
b = int(input("Enter number2 : "))

def gcd(a , b):
    if(a == b):
        print("GCD is : ", a)
    elif(a > b):
        gcd = 0
        for i in range(1, b + 1):
            if(a % i == 0 and b % i == 0):
                gcd = i
        print("GCD is : ", gcd)
    else:
        gcd = 0
        for i in range(1, a + 1):
            if(a % i == 0 and b % i == 0):
                gcd = i
        print("GCD is : ", gcd)

gcd(a,b)