"""
Objective: output the number of characters in the variable word, then output its first character, then its last character.
Restriction: your code must still work if the value of word is changed.
"""

word = "superfluous"

print(len(word))
print(word[0]) # indexing starts at 0, not 1.
print(word[-1]) # negative indexes count backward from the end.

print(word[len(word) - 1]) # this also works for the last character, but is more to type. word[len(word)] would produce an error, since the last index is one less than the length.