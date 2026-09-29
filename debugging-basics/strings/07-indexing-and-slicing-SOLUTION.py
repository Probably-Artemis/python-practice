"""
Objective: the code below should output the first three characters of word, then its last character. There are two bugs. Find them and fix them.
Restriction: your code must still work if the value of word is changed.
"""

word = "python"

print(word[0:3]) # indexing starts at 0, so [1:3] skipped the first character and stopped too soon.
print(word[len(word) - 1]) # the last index is one less than the length. word[len(word)] raises an IndexError. word[-1] also works.