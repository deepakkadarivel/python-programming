"""
    Check whether a string is a palindrome or not

    Conditional checks
    1. one letter by default is a palindrome.
    2. String can contain no letters, we call a string with no letters as an empty string.
        (An empty string is also a palindrome)


    Logical check
    1. First and last letter should be the same else it is not a palindrome.
    2. Strip the First and Last letter, and recheck the first and last of substring to be the same.


    Pseudo code
    1. If the string is made of no letters or one letter then it is a palindrome.
    2. Otherwise, compare first and last letter of the string.

        - if the first and last letter differ, then the string is not a palindrome
        - otherwise, the first and last letter is the same, Strip them from the string, and determine the
            string that remains is a palindrome. -- Repeat --

"""

word = input('Enter word: ')

word_len = len(word)

while True:
    if word_len == 0 or word_len == 1:
        print(word, 'is a palindrome')
        break
    if word[0] == word[word_len-1]:
        word_len -= 2
        continue
    else:
        print(word, 'is not a palindrome')
        break

