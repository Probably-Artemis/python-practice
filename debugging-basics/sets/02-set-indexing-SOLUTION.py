"""
Objective: the code below should output whichever color in colors comes first alphabetically, but it raises an error instead. Find the bug and fix it.
"""

colors = {"red", "green", "blue"}

print(sorted(colors)[0]) # sets are unordered, so they cannot be indexed, which raises a TypeError. sorted() returns a list, which can be.