"""
Objective: using a list comprehension, build a list holding "pass" for every score in scores of 60 or above and "fail" for every other score. Then, using a second comprehension, build a copy of readings where every negative number is replaced with 0. Output both lists.
Restriction: you may not edit preexisting code.
"""

scores = [72, 45, 90, 59, 60]

readings = [5, -2, 8, -1, 0, 3]

results = ["pass" if s >= 60 else "fail" for s in scores] # x if condition else y is a conditional expression. it produces one of two values.
clamped = [r if r >= 0 else 0 for r in readings]

print(results)
print(clamped)

# an if/else at the front picks what each item becomes, and every item is kept. an if at the end, like in 02, decides which items are kept at all.