"""
Objective: run the code below, and notice that original changes even though only backup was changed. Leave a comment explaining why, then fix it so that changing backup leaves original alone.
Restriction: you may only edit the line that creates backup.
"""

original = [1, 2, 3]

# backup = original doesn't make a new list. it gives the same list a second name, so a change made through either name shows up in both.
backup = original.copy() # .copy() builds a new list holding the same items. original[:] and list(original) work too.

backup.append(4)

print(original)
print(backup)