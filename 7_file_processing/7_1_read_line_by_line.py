"""
    Write a program to read through a file and print the contents of the file (line by line) all in upper case.

    Pseudo code
    1. Read file
    2. Iterate through each line
    3. rstrip the line
    4. convert the line to upper case
    5. print each line
"""

f_hand = open('7_file_processing/mbox-short.txt')

for line in f_hand:
    line = line.rstrip()
    print(line.upper())
