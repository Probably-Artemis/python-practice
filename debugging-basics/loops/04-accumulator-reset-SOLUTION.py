"""
Objective: the code below should output the sum of the numbers 1 through 5, which is 15, but the output is wrong. Find the bug and fix it.
"""

total = 0 # this was inside the loop, so total was reset to 0 on every iteration.

for i in range(1, 6):
    total += i

print(total)