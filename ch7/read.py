fName = input("Enter File Name: ")
try:
    fh = open(fName)
except:
    print("File cannot be opened : ", fName)
    quit()
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count +=1
    xConfidencePoint = line.find(":")
    xConfidenceValue = float(line[xConfidencePoint+1:])
    total = total + xConfidenceValue
    line = line.rsplit()
print("Average Spam Confidence:" , total/count)

