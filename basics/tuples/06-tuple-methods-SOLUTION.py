"""
Objective: rolls holds the results of rolling a six-sided die several times. Output how many times a 6 was rolled, the index of the first 6, the highest and lowest rolls, and whether a 5 was ever rolled.
Restriction: you may not edit preexisting code.
"""

rolls = (4, 2, 6, 6, 1, 6, 3)

print(rolls.count(6))
print(rolls.index(6)) # index() raises a ValueError if the item isn't in the tuple.
print(max(rolls))
print(min(rolls))
print(5 in rolls)

# count() and index() are the only two methods tuples have. anything that would change the tuple, like append() or sort(), does not exist.