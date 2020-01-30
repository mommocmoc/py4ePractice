fName = input("Enter File Name: ")

try:
    fHandler = open(fName)
except:
    print("There is no file such the name: ", fName)
    quit()
wordList = list()

for line in fHandler:
    line = line.split()
    for word in line:
        if word not in wordList : 
            wordList.append(word)
wordList.sort()        
print(wordList)
