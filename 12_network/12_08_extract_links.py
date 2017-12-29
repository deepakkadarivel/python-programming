import urllib.request
from bs4 import BeautifulSoup
import sys

url = input('Enter url: ')
position = input('Enter position: ')
repeat_count = input('Enter repeat count: ')

try:
    position = int(position)
except ValueError:
    print('Invalid number for position')
    sys.exit(0)

try:
    repeat_count = int(repeat_count)
except ValueError:
    print('Invalid number for repeat count')
    sys.exit(0)


for i in range(repeat_count):
    html = urllib.request.urlopen(url)

    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    print(i)
    url = tags[position].get('href', None)
    print(url)
