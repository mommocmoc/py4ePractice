import re

hand = open('../mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:',line) : #line.startswith('From:')
        print(line)
    #. : 어떤 문자이던
    #* : 뒤에 몇 글자가 있던 상관 없다
    # ex) ^X.* => X로 시작하는 뒤에 아무 문자 오는 거
    # \s : matches whitespace character
    # \S : matches non-whitespace character
    # + : 뒤에 한글자 이상 있어야됨
    # ex) ^X-\S+: => 'X-'로 시작하고 non-whitespace가 한글자이상이고 : 가 포함된 거

