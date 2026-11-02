"""
Objective: ask the user for a whole number and output double that number. If the user enters something that is not a whole number, output "that is not a whole number" instead of producing an error.
"""

try:
    number = int(input("Whole number: ")) # if this line raises a ValueError, python jumps straight to the except block.
    print(number * 2)
except ValueError:
    print("that is not a whole number")