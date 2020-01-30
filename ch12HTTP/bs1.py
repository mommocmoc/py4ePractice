import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup

# url = input('Enter Url -')
# test data
# url = 'http://py4e-data.dr-chuck.net/comments_42.html'
# actual data
url = 'http://py4e-data.dr-chuck.net/comments_132854.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup.find_all('span',{'class':'comments'})
commentsNums = list()
for tag in tags:
    commentsNums.append(int(tag.string))

print('Count ', len(tags))
print('Sum ',sum(commentsNums))
