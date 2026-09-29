"""
Objective: build a new dictionary with the keys and values of codes swapped, so that 1 maps to "a" and so on. Output the new dictionary.
Restriction: you may not edit preexisting code.
"""

codes = {"a": 1, "b": 2, "c": 3, "d": 4}

inverted = {}

for key, value in codes.items():
    inverted[value] = key

print(inverted)

# keys must be unique, but values do not have to be. if two keys shared a value, only the last one would survive the swap.
# a dictionary comprehension does the same in one line: {value: key for key, value in codes.items()}