"""
Objective: output the letter grade for score. 90 and above is an A, 80 to 89 is a B, 70 to 79 is a C, 60 to 69 is a D, and anything below 60 is an F.
Restriction: your code must still work if the value of score is changed.
"""

score = 84

if score >= 90:
    print("A")
elif score >= 80: # we only get here if score was below 90, so there's no need to also check score < 90.
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")