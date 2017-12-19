"""
    “Write a program to prompt for a file name, and then read through the file and look for lines of the form:
    X-DSPAM-Confidence:0.8475”

    Pseudo code
    1. Read file name from user
    2. open file
    3. Handle No file exception
    4. Iterate through files for text and increment count
    5. print total count
"""

import sys

file_name = input('Enter file name: ')

try:
    file_hand = open(file_name)
except OSError:
    print('File cannot be opened:', file_name)
    sys.exit(0)

search_value = 'X-DSPAM-Confidence:'
count = 0
line_count = 0

for line in file_hand:
    if line.startswith(search_value):
        value_pos = line.find(':')
        value = line[value_pos+1:].strip()

        count += float(value)
        line_count += 1

try:
    average = count/line_count
except ZeroDivisionError:
    print('Zero lines found with for', search_value)
    sys.exit(0)

print('Average spam confidence:', count/line_count)
