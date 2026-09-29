"""
Objective: the code below should ask the user for a price, then output that price doubled. Entering 4.99 should output 9.98, but it raises an error instead. Find the bug and fix it.
"""

price = float(input("Price: ")) # int() cannot convert a string holding a decimal point, which raises a ValueError. float() can.

print(price * 2)