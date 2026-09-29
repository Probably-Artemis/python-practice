"""
Objective: the code below should output True if x is between 1 and 10, including 1 and 10. Since x is 15, it should output False, but the output is wrong. Find the bug and fix it.
"""

x = 15

in_range = x >= 1 or x <= 10

print(in_range)