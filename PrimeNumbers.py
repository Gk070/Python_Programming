# Print prime numbers less than 1000
import math

n = int(input("Enter number : "))

print("Prime numbers are :\t")

for i in range(2, n):
    isPrime = 1
    for j in range(2, math.isqrt(i) + 1 ): # isqrt returns integer part of the number
        if i % j == 0:
            isPrime = 0
            break
    if isPrime == 1:
        print(i, end = " ")