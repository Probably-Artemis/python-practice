"""
Objective: every value in python can be treated as True or False. Before running anything, write a comment guessing what bool() will give back for each of these: 0, 7, -1, 0.0, "", " ", "False". Then output each one to check your guesses.
"""

print(bool(0)) # False
print(bool(7)) # True
print(bool(-1)) # True. any number other than zero is True, even negative ones.
print(bool(0.0)) # False
print(bool("")) # False. an empty string is False.
print(bool(" ")) # True. a string holding a single space is not empty.
print(bool("False")) # True. python doesn't read the words inside a string, it only checks whether the string is empty.