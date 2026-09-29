"""
Objective: build a dictionary that groups the words in words by their first letter, so that each letter maps to a list of the words starting with it. Output the dictionary.
Restriction: you may not edit preexisting code, and you may not import anything.
"""

words = ["apple", "banana", "avocado", "cherry", "blueberry", "cranberry", "apricot"]

groups = {}

for word in words:
    letter = word[0]

    if letter not in groups: # a key must exist before we can append to its list.
        groups[letter] = []

    groups[letter].append(word)

print(groups)

# groups.setdefault(letter, []).append(word) does the check and the append in one line.