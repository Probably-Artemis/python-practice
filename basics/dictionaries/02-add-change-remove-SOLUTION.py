"""
Objective: add cherries to stock with a quantity of 30, change the quantity of bananas to 10, then remove apples entirely. Output stock after every step.
Restriction: you may not edit preexisting code.
"""

stock = {"apples": 12, "bananas": 6}

stock["cherries"] = 30 # assigning to a key that doesn't exist yet creates it.
print(stock)

stock["bananas"] = 10 # assigning to a key that already exists replaces its value.
print(stock)

del stock["apples"] # stock.pop("apples") also works, and returns the removed value.
print(stock)