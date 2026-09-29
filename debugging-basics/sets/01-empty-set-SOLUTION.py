"""
Objective: the code below should create an empty set, add "red" to it, and output it, but it raises an error instead. Find the bug and fix it.
"""

colors = set() # {} creates an empty dictionary, not an empty set. dictionaries have no add() method, which raises an AttributeError.

colors.add("red")

print(colors)