"""
    Sort words in alphabetical order

    Pseudo code

    1. Read string from user input
    2. Convert string to List of strings by space
    3. Use list.sort() to sort the strings in list

"""

sentence = input('Enter sentence: ')

sentence_list = sentence.split(' ')
sentence_list.sort()

for word in sentence_list:
    print(word)
