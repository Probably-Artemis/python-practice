"""
Objective: the code below should output the difference between each number in readings and the one after it, which is 3, 5, and -2, but it raises an error instead. Find the bug and fix it.
"""

readings = [10, 13, 18, 16]

for i in range(len(readings)):
    print(readings[i + 1] - readings[i])