hrs = input('Enter Hours:')
rate = input('Enter Rate:')

actual_work_hrs = 40
extra_hrs = 0

try :
    work_hrs = float(hrs)
except:
    print('Error, please enter numeric input')
try :
    work_rate = float(rate)
except:
    print('Error, please enter numeric input')

if work_hrs > actual_work_hrs:
    extra_hrs = work_hrs - actual_work_hrs

pay = ((actual_work_hrs * work_rate) + (extra_hrs * (work_rate * 1.5)))

print('Pay:', pay)
