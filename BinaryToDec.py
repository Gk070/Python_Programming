import math

n = int(input("Enter a binary number : "))
num = n
dec = 0
i = 0

while(num):
    digit = num % 10
    dec = dec + digit * math.pow(2, i)
    num = num // 10
    i += 1

print("Equivalent Decimal Number is : ", int(dec))