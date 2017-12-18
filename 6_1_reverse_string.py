"""
    Write a while loop that starts at the last character in the string
    and works it’s way through first character in the string, printing
    each letter in a separate line except backwards.

    TODO 1: Accept a string from io
    TODO 2: Find the length of the string
    TODO 3: decrement len and print character in len with new line
    TODO 4: stop iteration and once len is less than 0
"""

value_string = input('Enter a string: ')

value_length = len(value_string)

while value_length > 0:
    value_length -= 1
    print(value_string[value_length])
