"""
    Write a program that categorizes each mail message by which day of the week the commit was done.
    To do this look for lines that start with "From", then look for the third word and keep a running count of each
    of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

    Sample Line:

    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

    Sample Execution:

    python dow.py
    Enter a file name: mbox-short.txt
    {'Fri': 20, 'Thu': 6, 'Sat': 1}


    Pseudo code
    1. Read file name and open
    2. Process file line by line for line starting with "From"
    3. Lookup for third word and keep running count using dictionary
    4. print the dictionary
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
        line_dict[line_list[2]] = line_dict.get(line_list[2], 0) + 1

print(line_dict)

