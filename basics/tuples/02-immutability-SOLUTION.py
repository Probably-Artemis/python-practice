"""
Objective: change the first value of point to 5, then output point.
Restriction: point must still be a tuple when you are done.
"""

point = (3, 7)

point = (5, point[1]) # tuples are immutable, so point[0] = 5 raises a TypeError. we must build a new tuple instead.

print(point)