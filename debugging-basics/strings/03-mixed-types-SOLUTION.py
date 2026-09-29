"""
Objective: the code below should output "I am 20 years old.", but it raises an error instead. Find the bug and fix it.
"""

age = 20

print("I am " + str(age) + " years old.") # + cannot join a str and an int, which raises a TypeError. the int must be cast to a string first.