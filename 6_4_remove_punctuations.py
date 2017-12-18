"""
    Remove punctuations from a string

    Pseudo code
    1. Create a string with all punctuations
    2. Read the string as an user input
    3. Iterate through the string and compare each character for punctuations.
        - If matched don't append the character to new string
        - Otherwise append the character to new string
"""

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

sentence = input('Enter sentence: ')

no_punctuation_string = ''

for letter in sentence:
    if letter not in punctuations:
        no_punctuation_string += letter

print(no_punctuation_string)
