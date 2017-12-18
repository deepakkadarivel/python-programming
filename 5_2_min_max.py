# TODO 1: Read number input until input is 'done'                                               x
# TODO 2: Use try and except for non numeric input and continue                                 x
# TODO 3: Print min, & max from the input list of numbers once 'done' is provided as input      x
# TODO 4: Exception handling for empty list                                                     x

numbers = []


def operate_on_numbers():
    try:
        numbers_min = min(numbers)
        numbers_max = max(numbers)
        print('Min', numbers_min, 'Max', numbers_max)
    except ValueError:
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