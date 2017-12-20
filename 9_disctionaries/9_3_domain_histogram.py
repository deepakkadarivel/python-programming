"""
    This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

    python schoolcount.py
    Enter a file name: mbox-short.txt
    {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
    'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

    Pseudo code
    1. Read file name and open
    2. Process file line by line for line starting with "From"
    3. Lookup for second word and split with '@' delimiter
    4. keep running count for domain after '@' using dictionary
    4. Print dictionary
"""

import sys

file_name = input('Enter File Name: ')

try:
    file_hand = open(file_name)
except OSError:
    print('Cannot open file', file_name)
    sys.exit(0)

line_dict = dict()

for line in file_hand:
    line_list = line.strip().split()
    if len(line_list) > 0 and line_list[0] == 'From':
        domain = line_list[1].split('@')[1]
        line_dict[domain] = line_dict.get(domain, 0) + 1

print(line_dict)