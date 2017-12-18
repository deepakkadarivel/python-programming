# TODO 1: Prompt for a score between 0.0 and 1.0    x
# TODO 2: Print an Error for out of range score     x
# TODO 3: Print a grade for score in range          x
# TODO 4: Optimize worst case scenario for if       -
# TODO 5: Create a function named computegrade which accepts score and returns a grade string

score = input("Enter Score:")
try:
    score = float(score)
except ValueError:
    print('Bad score')
    quit()

def computegrade(score):
    if score > 1.0 or score < 0.0:
        return 'Bad score'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'

grade = computegrade(score)
print(grade)
