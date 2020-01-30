import urllib.request, urllib.error, urllib.parse

fhand = urllib.request.urlopen('http://data.pr4e.org/mbox.txt')

for line in fhand:
    line = line.decode()
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    organization = email[email.find('@')+1:]
    print(organization)
    # words = line.decode().split()
    # for word in words:
    #     counts[word] = counts.get(word, 0) + 1
