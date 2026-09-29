"""
Objective: the code below should remove every item with a quantity of 0 from stock, then output stock. It raises an error instead. Find the bug and fix it.
"""

stock = {"apples": 0, "bread": 4, "eggs": 0, "milk": 8}

for item in stock:
    if stock[item] == 0:
        del stock[item]

print(stock)