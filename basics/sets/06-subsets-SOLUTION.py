"""
Objective: a recipe needs every ingredient in required. Output True if pantry holds all of them, and False otherwise. Then output which ingredients are missing, in alphabetical order.
Restriction: you may not edit preexisting code, you may not use loops, and your code must still work if either set is changed.
"""

required = {"flour", "eggs", "sugar", "butter"}

pantry = {"flour", "sugar", "milk", "butter", "salt"}

print(required <= pantry) # <= checks whether every item on the left is also on the right. required.issubset(pantry) is equivalent.
print(sorted(required - pantry))