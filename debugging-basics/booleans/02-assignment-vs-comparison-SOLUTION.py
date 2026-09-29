"""
Objective: the code below should output whether x is equal to 5, but it raises an error instead. Find the bug and fix it.
"""

x = 5

print(x == 5) # = assigns a value, while == compares two values. inside print(), x = 5 was read as a keyword argument, which raises a TypeError.