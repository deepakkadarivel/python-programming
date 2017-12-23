"""
    Write a program to look for lines of the form

    `New Revision: 39772`

    and extract the number from each of the lines using a regular expression and the findall() method.
    Compute the average of the numbers and print out the average.

    Enter file:mbox.txt
    38549.7949721

    Enter file:mbox-short.txt
    39756.9259259
"""

import re
import sys

file_name = input('Enter file:')

try:
    file_hand = open(file_name)
except OSError:
    print('Cannot open file.')
    sys.exit(0)

numbers = list()
for line in file_hand:
    values = re.findall('^N.+?: ([0-9.]+)', line)
    if len(values) > 0:
        numbers.extend(list(map(int, values)))

print(sum(numbers) / len(numbers))
