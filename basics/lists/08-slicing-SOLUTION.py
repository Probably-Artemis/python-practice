"""
Objective: using slicing, output the first three items of letters, then the last two, then every other item starting with the first, then the whole list reversed.
Restriction: you may not edit preexisting code.
"""

letters = ["a", "b", "c", "d", "e", "f", "g"]

print(letters[:3]) # slicing works on lists exactly the way it works on strings.
print(letters[-2:])
print(letters[::2])
print(letters[::-1])