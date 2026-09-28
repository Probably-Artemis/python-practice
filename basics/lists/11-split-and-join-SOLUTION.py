"""
Objective: split sentence into a list of words and output the list. Then output how many words there are. Finally, join the words back together with dashes between them instead of spaces, and output the result.
Restriction: you may not edit preexisting code.
"""

sentence = "the quick brown fox jumps over the lazy dog"

words = sentence.split() # with nothing in the parentheses, split breaks the string apart wherever there's whitespace.

print(words)
print(len(words))
print("-".join(words))