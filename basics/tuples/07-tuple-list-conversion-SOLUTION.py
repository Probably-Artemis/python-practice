"""
Objective: add the number 100 to scores, then sort it from highest to lowest and output it.
Restriction: scores must still be a tuple when you are done.
"""

scores = (72, 95, 88, 61)

temp = list(scores) # lists are mutable, so we convert, make our changes, then convert back.
temp.append(100)
temp.sort(reverse=True)
scores = tuple(temp)

print(scores)

# this also works in one line. + joins two tuples into a new one, and sorted() accepts any iterable but always returns a list.
# scores = tuple(sorted(scores + (100,), reverse=True))