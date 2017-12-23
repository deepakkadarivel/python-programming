"""
    Finding Numbers in a Haystack

    you will read through and parse a file with text and numbers.
    You will extract all the numbers in the file and compute the sum of the numbers.
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
# for line in file_hand:
#     values = re.findall('([0-9]+)', line)
#     if len(values) > 0:
#         numbers.extend(list(map(int, values)))

numbers = re.findall('([0-9]+)', file_hand.read())

print(sum(list(map(int, numbers))))
