"""
Objective: the code below should output the letter grade for score. 90 and above is an A, 80 to 89 is a B, 70 to 79 is a C, 60 to 69 is a D, and anything below 60 is an F. A score of 95 should output A, but the output is wrong. Find the bug and fix it.
Restriction: your code must still work if the value of score is changed.
"""

score = 95

if score >= 60:
    print("D")
elif score >= 70:
    print("C")
elif score >= 80:
    print("B")
elif score >= 90:
    print("A")
else:
    print("F")