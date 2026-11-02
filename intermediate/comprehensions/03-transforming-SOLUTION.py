"""
Objective: using a list comprehension, build a list of the words in words with the extra spaces removed and in all lowercase, and output it. Then, using a second comprehension, build a list of the lengths of those cleaned words and output that.
Restriction: you may not edit preexisting code.
"""

words = ["  Apple", "BANANA ", " cherry ", "Kiwi"]

cleaned = [w.strip().lower() for w in words] # the expression at the front can be anything, including method calls.
lengths = [len(w) for w in cleaned]

print(cleaned)
print(lengths)