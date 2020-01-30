fName = input("Enter File Name: ")

try:
    fHandler = open(fName)
except:
    print("There is no file such the name: ", fName)
    quit()
timeStampDict = dict()
for line in fHandler:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    line = line.split()
    for word in line:
        if word.find(":") == -1 : continue
        time = word.split(":")
        if time[0] not in timeStampDict:
            timeStampDict[time[0]] = 1
        else :
            timeStampDict[time[0]] = timeStampDict[time[0]] +1
sortedTimeStamp = list()
sortedTimeStamp = sorted(timeStampDict.items())
for k,v in sortedTimeStamp:
    print(k,v)
