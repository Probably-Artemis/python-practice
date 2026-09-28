"""
Objective: using slicing, output the first three characters of word, then the last three characters, then the whole word reversed.
Restriction: your code must still work if the value of word is changed.
"""

word = "mississippi"

print(word[:3]) # a slice includes the start index but stops just before the end index. leaving the start blank means "from the beginning."
print(word[-3:]) # leaving the end blank means "all the way to the end."
print(word[::-1]) # the third number is the step. a step of -1 iterates through the string backward.