alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str1 = input("Enter String : ")

for i in range(len(str1)):
    x = alph.index(str1[i])
    x = (x + 3) % 26
    str1[i] = alph[x]

print("Encrypted name is : ", str1)