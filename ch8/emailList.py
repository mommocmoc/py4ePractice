fName = input("Enter File Name: ")

try:
    fHandler = open(fName)
except:
    print("There is no file such the name: ", fName)
    quit()
emailList = list()
count = 0

for line in fHandler:
    if line.startswith("From:"):
        continue
    if not line.startswith("From"):
        continue
    
    if line.startswith("From"):
        line = line.split()
        print(line[1])
        count += 1
print("I found ",count,"E-mail Addresses.")