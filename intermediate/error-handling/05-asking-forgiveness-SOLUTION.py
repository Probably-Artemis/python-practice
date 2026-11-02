"""
Objective: ask the user for an item and output how many of it are in stock. If the item is not in stock, output "not stocked".
Restriction: you may not edit preexisting code, and you may not use if statements or get(). Use try and except instead.
"""

stock = {"apples": 12, "bread": 4, "eggs": 30}

item = input("Item: ")

try:
    print(stock[item])
except KeyError: # looking up a missing key raises a KeyError.
    print("not stocked")
