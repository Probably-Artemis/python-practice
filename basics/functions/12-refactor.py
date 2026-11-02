"""
Objective: the code below works, but everything is crammed into one loop. Rewrite it using at least three functions: one that calculates an average, one that turns an average into a letter grade, and one that outputs the report for a single student. The output must stay exactly the same.
"""

grades = {
    "alex": [90, 85, 77],
    "sam": [68, 74, 81, 90],
    "jordan": [95, 99, 92]
}

for name in grades:
    total = 0
    for score in grades[name]:
        total += score
    average = total / len(grades[name])

    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"

    print(f"{name}: {average:.1f} ({letter})")