import urllib.parse
import urllib.error
import urllib.request
import sqlite3
import re
conn = sqlite3.connect('email.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
fname = input('Enter file name: ')
if (len(fname) < 1):
    #Local Data
    # fname = 'mbox.txt'
    #Online Data
    fname = 'http://data.pr4e.org/mbox.txt'
# File Handler for local Data
# fh = open(fname)
# File Handler for online Data
fh = urllib.request.urlopen('http://data.pr4e.org/mbox.txt')

orgDict = dict()
for line in fh:
    #online data must be decoded
    line = line.decode()
    if not line.startswith('From: '):
        continue
    #find domain(organization name) from email address
    pieces = line.split()
    email = pieces[1]
    organization = email[email.find('@')+1:]
    # counting organization 
    if  organization not in orgDict : 
        orgDict[organization] = 1
    else :
        orgDict[organization] += 1
#INSERT INTO SQL DB
for (org, count) in orgDict.items():
    #org변수랑 이름 같은 거  있는 줄 찾아봐
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts (org, count) VALUES (?,?)",(org,count))
    conn.commit()
sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"
#SQL 들어간 데이터 살펴보기
for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

cur.close()
