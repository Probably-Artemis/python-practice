"""
Objective: the code below should group the words in words by their first letter, so that each letter maps to a list of every word starting with it. It runs, but some words go missing. Find the bug and fix it.
"""

words = ["apple", "banana", "avocado", "cherry", "blueberry", "apricot"]

groups = {}

for word in words:
    if word[0] not in groups:
        groups[word[0]] = []
    groups[word[0]].append(word) # assigning a new list replaced whatever was already stored for that letter. appending adds to it instead.

print(groups)