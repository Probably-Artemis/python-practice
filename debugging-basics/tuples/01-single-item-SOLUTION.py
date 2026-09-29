"""
Objective: the code below should output the length of single, which is 1, but it raises an error instead. Find the bug and fix it.
"""

single = (5,) # without the trailing comma, (5) is simply the int 5, and len() of an int raises a TypeError.

print(len(single))