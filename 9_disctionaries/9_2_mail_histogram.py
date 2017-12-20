"""
    Write a program to read through a mail log, build a histogram using a dictionary to
    count how many messages have come from each email address, and print the dictionary.
    Add code to the above program to figure out who has the most messages in the file.

    Enter file name: mbox-short.txt
    {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
    'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
    'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
    'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
    'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
    'ray@media.berkeley.edu': 1}

    Pseudo code
    1. Read file name and open
    2. Process file line by line for line starting with "From"
    3. Lookup for second word and keep running count using dictionary
    4. Find the max key in dict and print
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
        line_dict[line_list[1]] = line_dict.get(line_list[1], 0) + 1

max_mail = max(line_dict, key=line_dict.get)
print(max_mail, line_dict[max_mail])
