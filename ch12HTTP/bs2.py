import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup

url = input('Enter Url: ')
try:
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))
except:
    print("Wrong Input.Count & Position must be a number")
# test data
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
# position = 18
# count = 7
# actual data
# url = 'http://py4e-data.dr-chuck.net/known_by_Sullivan.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup.find_all('a')
for i in range(count):
    print('Retrieving: ',url)
    url = tags[position-1].get('href')
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('a')
print('Retrieving: ', url)
