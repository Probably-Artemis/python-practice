"""
Objective: the code below should output True if x is between 1 and 10, including 1 and 10. Since x is 15, it should output False, but the output is wrong. Find the bug and fix it.
"""

x = 15

in_range = x >= 1 and x <= 10 # every number is either at least 1 or at most 10, so or made this always True. both conditions must hold.

print(in_range)