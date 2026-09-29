"""
Objective: the code below should remove duplicates from names while keeping the names in the order they first appeared, and output ['ada', 'grace', 'alan', 'linus']. It runs, but the order of the output can change from one run to the next. Run it a few times, then find the bug and fix it.
"""

names = ["ada", "grace", "alan", "ada", "linus", "grace"]

unique = []
seen = set()

for name in names: # sets are unordered, so converting to one and back loses the original order. a set is still useful for tracking what has been seen.
    if name not in seen:
        seen.add(name)
        unique.append(name)

print(unique)