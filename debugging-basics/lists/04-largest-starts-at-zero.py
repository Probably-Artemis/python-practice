"""
Objective: the code below should output the largest number in temps, which is -3, but the output is wrong. Find the bug and fix it.
Restriction: you may not use max().
"""

temps = [-12, -3, -8, -20]

largest = 0

for temp in temps:
    if temp > largest:
        largest = temp

print(largest)