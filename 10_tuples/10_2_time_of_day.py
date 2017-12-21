"""
    This program counts the distribution of the hour of the day for each of the messages.
    You can pull the hour from the "From" line by finding the time string and then splitting that string into parts
    using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line,
    sorted by hour as shown below.

    Sample Execution:

    python timeofday.py
    Enter a file name: mbox-short.txt
    04 3
    06 1
    07 1
    09 2
    10 3
    11 6
    14 1
    15 2
    16 4
    17 2
    18 1
    19 1

    Pseudo Code
    1. Read file form user input
    2. Parse file line by line and search for line starting with 'From'
    3. Split the line into words and get position of Time
    4. Use dictionary to count the occurrences of Time throughout the file
    5. Use tuples to create a sorted list of Time by Hour
"""

import sys

file_name = input('Enter File: ')

try:
    file_hand = open(file_name)
except OSError:
    print('Cannot open file')
    sys.exit(0)

hours = dict()

for line in file_hand:
    words = line.strip().split()

    if len(words) > 0 and words[0] == 'From':
        hour = words[5].strip().split(':')[0]
        hours[hour] = hours.get(hour, 0) + 1

sorted_hours = sorted([(key, value) for (key, value) in hours.items()])

for hour, count in sorted_hours:
    print(hour, count)
