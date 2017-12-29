"""
    Download image using urllib
"""

import urllib.request

url = input('Enter url: ')
img = urllib.request.urlopen(url).read()

f_hand = open('cover.jpg', 'wb')
f_hand.write(img)
f_hand.close()