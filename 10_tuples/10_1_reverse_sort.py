"""
    Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line.
    Count the number of messages from each person using a dictionary.

    After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples
    from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

    Sample Line:
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

    Enter a file name: mbox-short.txt
    cwen@iupui.edu 5

    Enter a file name: mbox.txt
    zqian@umich.edu 195


    Pseudo code
    1. Read file name from user input
    2. Parse file line by line and search for line starting with 'From'
    3. Split line into list of words and find address from second position
    4. Create a dictionary to hold address and count of the messages from that address
    5. Create tuple of (count, email) from dictionary and sort in reverse order.
    6. Print email with highest count

"""

import sys

file_name = input("Enter File: ")

try:
    file_hand = open(file_name)
except OSError:
    print('Cannot open file')
    sys.exit(0)

mails = dict()

for line in file_hand:
    words = line.strip().split()

    if len(words) > 0 and words[0] == 'From':
        mails[words[1]] = mails.get(words[1], 0) + 1

sorted_mail = sorted([(val, key) for (key, val) in mails.items()], reverse=True)
count, email = sorted_mail[0]
print(email, count)
