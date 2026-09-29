"""
Objective: the code below should ask the user for their age, then output how old they will be next year, but it raises an error instead. Find the bug and fix it.
"""

age = int(input("How old are you? ")) # input() always returns a string, and adding a str and an int raises a TypeError.

print("Next year you will be", age + 1)