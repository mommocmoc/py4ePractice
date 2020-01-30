import xml.etree.ElementTree as ET

data ='''
<person>
<name>JaeHwan</name>
<phone type="intl">+82 10 54535 1109</phone>
<email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print(tree.find('name').text)
print(tree.find('email').get('hide'))
