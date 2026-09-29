"""
Objective: the code below should output the number of vowels in word, which is 3, but the output is wrong. Find the bug and fix it.
"""

word = "banana"

vowels = 0

for letter in word:
    if letter in "aeiou":
        vowels + 1

print(vowels)