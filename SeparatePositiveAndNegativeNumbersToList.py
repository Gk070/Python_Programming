n = list(map(int, input("Enter numbers : ").split()))
positive = []
negative = []

for i in range(len(n)):
    if(n[i] >= 0):
        positive.append(n[i])
    else:
        negative.append(n[i])

print(positive)
print(negative)