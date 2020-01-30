import re

fhand = open('./regex_sum_132852.txt')
total = list()
for line in fhand:
    numInText = re.findall('[0-9]+',line)
    if len(numInText) == 0 : continue
    for num in numInText:
        total.append(int(num))
print(sum(total))

print(sum([int(n) for n in re.findall('[0-9]+', open('./regex_sum_132852.txt').read())]))
# for n in re.findall('[0-9]+', open('./regex_sum_132852.txt').read()):
    
    
