import xml.etree.ElementTree as ET
import urllib.request
import urllib.error
import urllib.parse

#sample
# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

#actual
# url = 'http://py4e-data.dr-chuck.net/comments_132856.xml'
url = input('Enter location:')
print('Retrieving',url)
data = urllib.request.urlopen(url,context='ctx').read()
print('Retrived',len(data),'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')
total = 0
for count in counts:
    total = total + int(count.text)
print('Count: ',len(counts))
print('Sum: ',total)

