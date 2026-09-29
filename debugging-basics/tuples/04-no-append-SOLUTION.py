"""
Objective: the code below should add 4 to the end of values and output (1, 2, 3, 4), but it raises an error instead. Find the bug and fix it.
Restriction: values must still be a tuple when you are done.
"""

values = (1, 2, 3)

values = values + (4,) # tuples have no append() method, which raises an AttributeError. + joins two tuples into a new one.

print(values)