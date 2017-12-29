import sys
import json
import urllib.request, urllib.parse

url = input('Enter url: ')
if len(url) < 1:
    sys.exit(0)

data = urllib.request.urlopen(url)
data = data.read().decode()

data = json.loads(data)

count = 0
for comment in data['comments']:
    count += comment['count']

print(count)
