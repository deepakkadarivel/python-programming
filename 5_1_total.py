# TODO 1: Read number input until input is 'done'                                   x
# TODO 2: Use try and except for non numeric input and continue                     x
# TODO 3: Print total, avg, & count of numbers once 'done' is provided as input     x
# TODO 4: Exception handling for zero division                                      x

numbers = []


def operate_on_numbers():
    try:
        numbers_len = len(numbers)
        numbers_sum = sum(numbers)
        numbers_avg = numbers_sum/numbers_len
        print('Total', numbers_sum, 'Average', numbers_avg, 'Count', numbers_len)
    except ZeroDivisionError:
        print('List empty')


def get_user_input():
    while True:
        number = input('Enter a number: ')
        if number == 'done':
            operate_on_numbers()
            break
        try:
            number = float(number)
            numbers.append(number)
        except ValueError:
            print('Invalid input')
            continue


get_user_input()
