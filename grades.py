# Define a function that accepts a percentage as an argument and
# returns a letter grade (A+, A, A-, B+, etc) for that percentage.
#
# Prompt your user to enter a percentage and display a message showing
# them the equivalent letter grade.

percentage = 0

def convert_to_grade(percentage):

    if percentage >= 95:
        return 'Your grade equivalent is A+'
    elif percentage < 95 and percentage >= 92:
        return 'Your grade equivalent is A'
    elif percentage < 92 and percentage >= 90:
        return 'Your grade equivalent is A-'
    elif percentage < 90 and percentage >= 85:
        return 'Your grade equivalent is B+'
    elif percentage < 85 and percentage >= 82:
        return 'Your grade equivalent is B'
    else:
        return 'Your grade equivalent is a B- or below'

print("Please enter a percentage")
percentage = int(input())

print(convert_to_grade(percentage))
