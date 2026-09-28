"""
Objective: output a sorted copy of scores without changing scores itself, then output scores to prove it is unchanged. Then sort scores in place from highest to lowest and output it.
Restriction: you may not edit preexisting code.
"""

scores = [72, 95, 88, 61, 79]

print(sorted(scores)) # sorted() makes a brand new list and leaves the original alone.
print(scores)

scores.sort(reverse=True) # .sort() changes the list itself and gives back None, so print(scores.sort()) would just output None.
print(scores)