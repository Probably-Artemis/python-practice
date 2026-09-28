"""
Objective: ask the user for their age, then output how old they will be next year.
"""

age = int(input("How old are you? ")) # input() always gives back a string, even when the user types a number. "19" + 1 would error.

print("Next year you will be", age + 1)