# Count the number of odd and even numbers in a set

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_count = 0
odd_count = 0

for num in numbers:
    if(num % 2 == 0):
        even_count += 1
    else:
        odd_count += 1

print("No of Odd Numbers is : ", odd_count)
print("No of Even Numbers is : ", even_count)