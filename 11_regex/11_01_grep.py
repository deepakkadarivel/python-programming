"""
    Write a simple program to simulate the operation of the grep command on Unix.
    Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

    $ python grep.py
    Enter a regular expression: ^Author
    mbox.txt had 1798 lines that matched ^Author

    $ python grep.py
    Enter a regular expression: ^X-
    mbox.txt had 14368 lines that matched ^X-

    $ python grep.py
    Enter a regular expression: java$
    mbox.txt had 4218 lines that matched java$
"""

import re
import sys

reg_exp = input('Enter a regular expression: ')

file_name = '11_regex/mbox.txt'

try:
    file_hand = open(file_name)
except:
    print('Cannot open file')
    sys.exit(0)

count = 0

for line in file_hand:
    line.rstrip()
    lines = re.findall(reg_exp, line)
    if len(lines) > 0:
        count += 1

print('mbox.txt had', count, 'lines that matched', reg_exp)
