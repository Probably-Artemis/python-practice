"""
Objective: build a new list holding each item from names only once, in the order they first appeared. Output the new list.
Restriction: you may not edit preexisting code, and you may not use set() or dict().
"""

names = ["ada", "grace", "alan", "ada", "linus", "grace", "ada"]

unique = []

for name in names:
    if name not in unique:
        unique.append(name)

print(unique)

# set(names) would also remove the duplicates, but sets don't keep things in order.