"""
Objective: output each student's average grade, rounded to one decimal place. Then output the name of the student with the highest average.
Restriction: you may not edit preexisting code, and your code must still work if students are added or removed.
"""

grades = {
    "alex": [90, 85, 77],
    "sam": [68, 74, 81, 90],
    "jordan": [95, 99, 92]
}

best_name = ""
best_average = -1 # starting below any possible average means the first student always replaces it.

for name, scores in grades.items(): # values can be any type, including lists.
    average = sum(scores) / len(scores)
    print(name, round(average, 1)) # a value exactly halfway rounds to the nearest even digit, so sam's 78.25 becomes 78.2, not 78.3.

    if average > best_average:
        best_name = name
        best_average = average

print("Highest average:", best_name)