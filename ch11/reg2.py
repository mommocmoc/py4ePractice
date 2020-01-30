import re

x = 'My 2 favorite numbers are 19 and 42'
#[0-9] : 숫자가 들어간
# + : 한자리 이상 문자
y = re.findall('[0-9]+',x)
print(y)

y = re.findall('[M].+?',x)
print(y)

x = 'From: Using the : character'
#Greedy : 찾은 조건 중 가장 긴 것
y = re.findall('^F.+:', x)
print(y)
#Non-greedy : 찾은 조건 중 짧은 것
y= re.findall('^F.+?:',x)
print(y)

x = 'From stephen@uct.ac.za SAT Jan ~~'
# ()를 이용해 추출하고 싶은 영역 지정이 가능
y = re.findall('^From \S+@\S+',x)
print(y)
y = re.findall('^From (\S+@\S+)',x)
print(y)
#[^ ] => Not a blank
y= re.findall('^From .*@([^ ]*)',x)
print(y)
