"""
Objective: the code below should ask the user for a number, then output "big" if it is greater than 10 and "small" otherwise. It raises an error instead. Find the bug and fix it.
"""

number = int(input("Enter a number: ")) # input() returns a string, and comparing a str to an int with > raises a TypeError.

if number > 10:
    print("big")
else:
    print("small")