"""
    Scrape web page using urllib and regular expression
"""

import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_name = input('Enter url: ')

file_hand = urllib.request.urlopen(url_name, context=ctx).read()

links = re.findall(b'href="(http://.+?)"', file_hand)

for link in links:
    print(link.decode())
