"""
Objective: the code below should remove duplicates from names while keeping the names in the order they first appeared, and output ['ada', 'grace', 'alan', 'linus']. It runs, but the order of the output can change from one run to the next. Run it a few times, then find the bug and fix it.
"""

names = ["ada", "grace", "alan", "ada", "linus", "grace"]

unique = list(set(names))

print(unique)