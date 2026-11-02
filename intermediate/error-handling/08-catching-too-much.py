"""
Objective: the code below should add up the numbers in values, skipping any that are not numbers, and output 70. Instead it outputs 0 and no error appears. Find the bug, fix it, then change the except so that a mistake like this one can never be hidden again.
"""

values = ["10", "20", "x", "40"]

total = 0

for value in values:
    try:
        total += int(valeu)
    except:
        pass

print(total)