"""
Objective: the code below should output scores sorted from lowest to highest, but the output is wrong. Find the bug and fix it.
"""

scores = [72, 95, 88, 61, 79]

sorted_scores = sorted(scores) # .sort() sorts in place and returns None. sorted() returns a new sorted list.

print(sorted_scores)