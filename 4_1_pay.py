# TODO 1: Remove bare expect and use valid value check except
# TODO 2: Create a function named computepay which takes 2 parameters (hours & rate)
# INFO : Can replace quit() with sys.exit(0)

work_hrs = input('Enter Hours:')
try:
    work_hrs = float(work_hrs)
except ValueError:
    print('Error, please enter numeric input')
    quit()

rate = input('Enter Rate:')
try:
    rate = float(rate)
except ValueError:
    print('Error, please enter numeric input')
    quit()


def computepay(hours, rate):
    actual_work_hrs = 40
    extra_hrs = (hours - actual_work_hrs)
    extra_work_hrs = extra_hrs if extra_hrs > 0 else 0
    pay = (actual_work_hrs * rate) + (extra_work_hrs * (rate * 1.5))
    return pay


pay = computepay(work_hrs, rate)
print('Pay', pay)
