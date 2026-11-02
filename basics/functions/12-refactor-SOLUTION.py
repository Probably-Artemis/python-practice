"""
Objective: the code below works, but everything is crammed into one loop. Rewrite it using at least three functions: one that calculates an average, one that turns an average into a letter grade, and one that outputs the report for a single student. The output must stay exactly the same.
"""

grades = {
    "alex": [90, 85, 77],
    "sam": [68, 74, 81, 90],
    "jordan": [95, 99, 92]
}

def average(scores):
    return sum(scores) / len(scores)

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def print_report(name, scores):
    avg = average(scores)
    print(f"{name}: {avg:.1f} ({letter_grade(avg)})")

for name, scores in grades.items():
    print_report(name, scores)

# each function now does one job and has a name saying what that job is. letter_grade can be reused elsewhere and tested on its own.