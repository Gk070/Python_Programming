n = int(input("Enter number : "))
y = int(input("Enter power : "))

def power(n, y):
    newN = 1
    if(y == 1):
        newN = n
    for i in range(2, y + 1):
        newN = newN * n
    print("Number ", n, " ^ ", y , " is ", newN)


power(n, y)