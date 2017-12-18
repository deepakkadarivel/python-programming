"""
    Find the count of a letter in a word. Encapsulate the code in a function named count,
    and generalize it so that it accepts the string and letter as an argument.

    TODO 1: Accept input for a word and letter to search for.
    TODO 2: Define a count function that accepts word and letter as parameter to count the number of occurrences in word.
        - Define a variable that will increment for each occurrence of letter
        - print the total count
"""


def count(word, letter):
    letter_count = 0
    for character in word:
        if character == letter:
            letter_count = letter_count + 1

    print(letter_count)


word_input = input('Enter Word: ')
letter_input = input('Enter Letter: ')

count(word_input, letter_input)
