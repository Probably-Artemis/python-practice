"""
Objective: count how many times each letter appears in word, store the counts in a dictionary, and output the dictionary.
Restriction: you may not edit preexisting code, and you may not use count().
"""

word = "mississippi"

counts = {}

for letter in word:
    counts[letter] = counts.get(letter, 0) + 1 # get() returns 0 the first time a letter is seen, so there's no need to check whether the key exists.

print(counts)

# python's collections module has a Counter class that does this for you, but that isn't the point.