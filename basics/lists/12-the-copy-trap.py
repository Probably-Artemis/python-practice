"""
Objective: run the code below, and notice that original changes even though only backup was changed. Leave a comment explaining why, then fix it so that changing backup leaves original alone.
Restriction: you may only edit the line that creates backup.
"""

original = [1, 2, 3]

backup = original

backup.append(4)

print(original)
print(backup)