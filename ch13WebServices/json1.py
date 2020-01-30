import json
import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup as bs

#Test data link
link1 = 'http://py4e-data.dr-chuck.net/comments_42.json'

# Actual data link
link2 = 'http://py4e-data.dr-chuck.net/comments_132857.json'

#Read data from URL
data = urllib.request.urlopen(link2).read()
#Parsing
soup = bs(data,'html5lib')
#Extract JSON data in body tag
soup = soup.find('body')
jsonData = soup.text
#Load json text to json
jsonData = json.loads(jsonData)
#Extract 'comments' data including 'name', 'count' data 
resultData = jsonData['comments']
#Make countList for handling count data
countList = list()
#Extract 'count' data from resultData list
for item in resultData:
    countList.append(int(item['count']))

print('Count:', len(resultData))
print('Sum:',sum(countList))
