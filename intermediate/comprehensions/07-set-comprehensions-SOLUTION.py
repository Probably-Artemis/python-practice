"""
Objective: using a set comprehension, build a set of the first letter of every word in sentence, ignoring capitalization. Output the letters in alphabetical order.
Restriction: you may not edit preexisting code.
"""

sentence = "Big bears built boats while wolves watched quietly"

letters = {w[0].lower() for w in sentence.split()} # curly braces without a colon make a set, so each letter is kept only once.

print(sorted(letters))