"""
Objective: the code below should group the words in words by their first letter, so that each letter maps to a list of every word starting with it. It runs, but some words go missing. Find the bug and fix it.
"""

words = ["apple", "banana", "avocado", "cherry", "blueberry", "apricot"]

groups = {}

for word in words:
    groups[word[0]] = [word]

print(groups)