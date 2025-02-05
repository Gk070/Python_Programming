'''
Pattern 2
-------------
A
A B
A B C
A B C D
-------------
'''
n = int(input("Enter number of rows : "))
if(n <= 26):
    for i in range(ord('A'), ord('Z') + 1):
        for j in range(ord('A'), i + 1):
            print(chr(j), end = " ")
        print()
else:
    print("N > 26 Please Run The Program Again")