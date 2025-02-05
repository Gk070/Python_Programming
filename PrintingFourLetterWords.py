count = 0
inputfile = open("myfile.txt", "r")
for line in inputfile:
    wordslist = line.split()
    for words in wordslist:
        if(len(words) == 4):
            count += 1
print("Count of four-lettered words is : ", count)
