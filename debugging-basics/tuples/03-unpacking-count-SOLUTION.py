"""
Objective: the code below should output each value in color on its own line, but it raises an error instead. Find the bug and fix it.
"""

color = (255, 128, 0)

red, green, blue = color # the number of variables must match the number of items in the tuple, or python raises a ValueError.

print(red)
print(green)
print(blue)