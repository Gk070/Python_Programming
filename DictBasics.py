dict = {}

n = int(input("Enter the number of entries : "))

for i in range(n):
    key = input("Enter key : ")
    value = input("Enter value : ")
    dict[key] = value

def modify(n):
    key = input("Enter key which is to be updated : ")
    if(key in dict):
        value = input("Enter new name to be inserted : ")
        dict[key] = value
        print(value)
modify(n)

def delete(n):
    key = input("Enter key which is to be deleted : ")
    if(key in dict):
        del dict[key]
        print(key, " deleted succesfully")
        print(key)

delete(n)