alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encstr = ""

str1 = input("Enter String : ").upper()

for char in str1:
    if char in alph:
        x = alph.index(char)
        x = (x + 3) % 26
        encstr += alph[x]
    else:
        encstr += char

print("Encrypted name is : ", encstr)