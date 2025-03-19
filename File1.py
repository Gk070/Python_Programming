inputfile = open("myfile.txt", 'r')
x = input("Enter Substring : ")

def file(inputfile, x):
    wordsStartWithX = []
    indexOfx = []

    for line in inputfile:
        wordslist = line.split()
        for words in wordslist:
            if x in words:
                wordsStartWithX.append(words)
                indexOfx.append(words.index(x))
        if(wordsStartWithX == []):
            return ([],[])
        return (wordsStartWithX, indexOfx)

result = file(inputfile, x)
print(result)

