"""
Objective: convert numbers into a set, then output the set and its length.
Restriction: you may not edit preexisting code.
"""

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

unique = set(numbers) # a set cannot hold duplicates, so every repeated value is dropped.

print(unique)
print(len(unique))

# sets are unordered. with small integers they often print in order, but that is not guaranteed.