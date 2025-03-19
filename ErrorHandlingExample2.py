import math
import sys

try:
    result = math.factorial(2.4)
except:
    print("Something has happened")
else:
    print("Factorial is : ", result)
finally:
    print("Already did everythig")