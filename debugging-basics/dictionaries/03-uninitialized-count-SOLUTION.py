"""
Objective: the code below should count how many times each letter appears in word and output the counts, but it raises an error instead. Find the bug and fix it.
"""

word = "banana"

counts = {}

for letter in word:
    counts[letter] = counts.get(letter, 0) + 1 # += reads the current value first, and on a letter's first appearance there is no value to read, which raises a KeyError.

print(counts)