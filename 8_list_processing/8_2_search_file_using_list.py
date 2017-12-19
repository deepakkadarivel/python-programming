"""
    Write a program to read through the mail box data and when you find line that starts with From,
    you will split the line into words using the split function. We are interested in who sent the message,
    which is the second word on the From line.

    From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

    You will parse the From line and print out the second word for each From line,
    then you will also count the number of From (not From:) lines and print out a count at the end.

"""
import sys

try:
    file_hand = open('8_list_processing/mbox-short.txt')
except OSError:
    print('File cannot be opened')
    sys.exit(0)

parse_count = 0

for line in file_hand:
    line_list = line.strip().split()
    if len(line_list) > 0 and line_list[0] == 'From':
        print(line_list[1])
        parse_count += 1

print(parse_count)
