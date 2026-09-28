"""
Objective: output how many items are in fruits. Then ask the user for a fruit and tell them whether it's in the list.
Restriction: you may not edit preexisting code.
"""

fruits = ["apple", "banana", "cherry", "mango", "kiwi"]

print(len(fruits)) # len() works on lists the same way it works on strings.

choice = input("Name a fruit: ")

if choice.lower() in fruits: # in checks every item in the list for a match.
    print("Yes,", choice, "is in the list.")
else:
    print("No,", choice, "is not in the list.")