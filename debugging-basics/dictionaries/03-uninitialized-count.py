"""
Objective: the code below should count how many times each letter appears in word and output the counts, but it raises an error instead. Find the bug and fix it.
"""

word = "banana"

counts = {}

for letter in word:
    counts[letter] += 1

print(counts)