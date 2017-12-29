"""
    Retrieve span tags and count all values inside content.
"""

import urllib.request
from bs4 import BeautifulSoup

url = input('Enter url: ')

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, 'html.parser')

count = 0
tags = soup('span')
for tag in tags:
    count += int(tag.contents[0])

print(count)