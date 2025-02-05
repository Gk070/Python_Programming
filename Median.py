inputFile = open("numbers.txt", "r")
numbers = []
for line in inputFile:
    numslist = line.split()
    for num in numslist:
        numbers.append(int(num))

numbers.sort()
midpoint = len(numbers) // 2

print("Median is : ")

if(len(numbers) % 2 == 1):
    print(numbers[midpoint])
else:
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2)
