"""
Objective: using Counter from the collections module, count the letters in word, then output the counts and the two most common letters. Then, using defaultdict, group the words in words by their first letter and output the groups.
Restriction: you may not edit preexisting code.
"""

word = "mississippi"

words = ["apple", "banana", "avocado", "cherry", "blueberry", "apricot"]

from collections import Counter, defaultdict

counts = Counter(word) # a Counter is a dictionary that counts things for you.

print(counts)
print(counts.most_common(2))

groups = defaultdict(list) # a missing key is created automatically with the value list(), an empty list.

for w in words:
    groups[w[0]].append(w)

print(dict(groups))

# compare this with dictionaries/05 and dictionaries/10, which do the same jobs by hand.