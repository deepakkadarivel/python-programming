import sys
import urllib.request, urllib.parse
import xml.etree.ElementTree as ET

url = input('Enter url: ')
if len(url) < 1:
    sys.exit(0)

data = urllib.request.urlopen(url)
data = data.read().decode()

tree = ET.fromstring(data)
comments = tree.findall('comments/comment')

count = 0
for item in comments:
    count += int(item.find('count').text)
print(count)
