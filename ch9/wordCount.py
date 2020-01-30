fName = input("Enter File Name: ")

try:
    fHandler = open(fName)
except:
    print("There is no file such the name: ", fName)
    quit()
wordDict = dict()
for line in fHandler:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    line = line.split()
    word = line[1]
    if word not in wordDict:
        wordDict[word] = 1
    else:
        wordDict[word] = wordDict[word] + 1
bigWord = None
bigCount = 0
for word, count in wordDict.items():
    if count is 0 or count > bigCount:
        bigCount = count
        bigWord = word

print(bigWord, bigCount)
