"""
Objective: output how many unique words are in text, then output those words in alphabetical order. "The" and "the" should count as the same word.
Restriction: you may not edit preexisting code.
"""

text = "The cat and the dog and the bird all sat by the door and the cat slept"

words = set(text.lower().split())

print(len(words))
print(sorted(words))