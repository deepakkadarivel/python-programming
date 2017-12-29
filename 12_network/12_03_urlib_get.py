"""
    Request and read response using urllib
"""

import urllib.request

f_hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in f_hand:
    print(line.decode().strip())
