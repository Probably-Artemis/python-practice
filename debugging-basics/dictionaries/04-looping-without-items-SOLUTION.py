"""
Objective: the code below should output every item in prices on its own line, like "coffee: $3.50", but it raises an error instead. Find the bug and fix it.
"""

prices = {"coffee": 3.5, "bagel": 2.25, "tea": 3.0}

for item, price in prices.items(): # iterating over a dictionary directly gives only its keys. python then tried to unpack each key string into two variables, which raises a ValueError.
    print(f"{item}: ${price:.2f}")