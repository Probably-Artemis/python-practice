"""
Objective: count how many vowels (a, e, i, o, u) are in sentence and output the count.
Restriction: you may not edit preexisting code, and you may not use count().
"""

sentence = "Massachusetts Institute of Technology"

vowels = 0

for letter in sentence.lower(): # a for loop can iterate through a string one character at a time. lower() makes sure capital vowels get counted too.
    if letter in "aeiou": # in checks whether letter shows up anywhere inside "aeiou".
        vowels += 1

print(vowels)