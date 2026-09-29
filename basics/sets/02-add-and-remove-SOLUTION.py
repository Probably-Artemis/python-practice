"""
Objective: create an empty set. Add "red", "green", and "blue" to it one at a time, then add "red" a second time. Next, remove "green", and then try to remove "purple" without producing an error. Output the set after every step.
"""

colors = set() # {} creates an empty dictionary, not an empty set.

colors.add("red")
print(colors)

colors.add("green")
print(colors)

colors.add("blue")
print(colors)

colors.add("red") # adding an item that already exists does nothing.
print(colors)

colors.remove("green") # remove() raises a KeyError if the item is missing.
print(colors)

colors.discard("purple") # discard() does the same job, but does nothing if the item is missing.
print(colors)