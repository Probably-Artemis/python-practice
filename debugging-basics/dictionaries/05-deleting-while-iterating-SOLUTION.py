"""
Objective: the code below should remove every item with a quantity of 0 from stock, then output stock. It raises an error instead. Find the bug and fix it.
"""

stock = {"apples": 0, "bread": 4, "eggs": 0, "milk": 8}

for item in list(stock): # a dictionary cannot change size while it is being iterated over, which raises a RuntimeError. list(stock) makes a separate list of the keys to iterate over instead.
    if stock[item] == 0:
        del stock[item]

print(stock)