"""
Objective: ask the user for at least five words (a noun, a verb, an adjective, and so on), then output a short story that uses all of them.
"""

adjective = input("Adjective: ")
noun = input("Noun: ")
verb = input("Verb ending in -ing: ")
place = input("Place: ")
number = input("Number: ") # we leave this as a string because we won't be doing any math with it.

print(f"Once upon a time, a {adjective} {noun} was {verb} through {place}.")
print(f"It kept going for {number} days, until the professor finally noticed.")
print("The end.")