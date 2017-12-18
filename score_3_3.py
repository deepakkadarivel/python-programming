# TODO 1: Prompt for a score between 0.0 and 1.0    x
# TODO 2: Print an Error for out of range score     x
# TODO 3: Print a grade for score in range          x
# TODO 4: Optimize worst case scenario for if       -

score = input("Enter Score:")
try:
    score = float(score)
except ValueError:
    print('Bad score')
    quit()

if score > 1.0 or score < 0.0:
    print('Bad score')
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')
