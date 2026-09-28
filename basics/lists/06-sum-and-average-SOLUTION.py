"""
Objective: output the total of all the numbers in grades, then their average.
Restriction: you may not edit preexisting code, and you may not use sum(). Your code must still work if grades is changed.
"""

grades = [88, 92, 75, 64, 99, 81]

total = 0

for grade in grades:
    total += grade

average = total / len(grades)

print(total)
print(average)

# once you understand how it works, sum(grades) / len(grades) is the standard way to do this.
total = sum(grades)
average = sum(grades) / len(grades)