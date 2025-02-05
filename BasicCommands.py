import math # To import the module math

print(10 % 20)

print(int(6.5)) # returns only integer part

print(round(12.57)) # round to nearest integer

x = ['Apple', 'Mango', 'Banana']
print("Apple" in x)

i = 0
while(i < 3):
    print(i, end = " ")
    i += 1

# printing the number in reverse order 
for i in range(10, 1, -1):
    print(i, end = " ")

for i in range(1, 10, 2): # Range(1, 10, 2) means number from 1 - 10(excluding 10) and skipping 1 number
    print(i, end = " ") 

for i in range(1, 10): # Range(1, 10) means numbers from 1 - 10(excluding 10)
    print(i, end=" ")

for i in range(10): # To print first 9 numbers from 0 (Rangil kodukunnente 1 kurach loop execute avollu)
    print(i, end = " ") 

print(2 ** 3) # will print 2^3

print(chr(65)) # chr 65 is used to covert ASCII value to character

print(ord('A')) # ord 'A' to convert character to ASCII value

print(3*"Hi\n") # To print a string 3 times '\n' is used to move to next line

print(9/2) # / will return 4.5

print(9//2) # // will return only integer part

# This is called parsing 
num1 = input("Enter a number : ") # To read as string
num2 = input("Enter a number : ")
sum = num1 + num2 
print(sum) # will return the numbers combined since concatination occurs(str + str)
print(type(num1)) # type is used print the datatype of the variable

num3 = int(input("Enter a number : ")) # To read as integer 