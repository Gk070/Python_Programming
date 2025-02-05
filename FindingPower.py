n = int(input("Enter number : "))
y = int(input("Enter power : "))
if(y == 1):
    newN = n
for i in range(2, y + 1):
    newN = n * n
print("Number ", n, " ^ ", y , " is ", newN)