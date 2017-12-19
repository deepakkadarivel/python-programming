"""
    Write a program to open the file romeo.txt and read it line by line. For each line,
    split the line into a list of words using the split function.

    For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list.

    When the program completes, sort and print the resulting words in alphabetical order.
"""

import sys

try:
    file_hand = open('8_list_processing/romeo.txt')
except OSError:
    print('File cannot be opened')
    sys.exit(0)

file_list = list()
for line in file_hand:
    line_list = line.strip().split()

    for word in line_list:
        if word in file_list:
            continue
        file_list.append(word)

file_list.sort()
print(file_list)
