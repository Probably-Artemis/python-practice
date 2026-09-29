"""
Objective: the code below should change the first value of point to 5 and output (5, 4), but it raises an error instead. Find the bug and fix it.
Restriction: point must still be a tuple when you are done.
"""

point = (3, 4)

point = (5, point[1]) # tuples are immutable, so assigning to point[0] raises a TypeError. we must build a new tuple instead.

print(point)