n = list(map(int, input("Enter the numbers : ").split()))

def min_max(n):
    n.sort()
    print("Largest number is : ", n[0])
    print("Smallest number is : ", n[len(n) - 1])

min_max(n)