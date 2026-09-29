"""
Objective: output every item in prices on its own line, like "coffee: $3.50". Then output only the item names, one per line. Finally, output the total of all the prices.
Restriction: you may not edit preexisting code, and your code must still work if items are added to or removed from prices.
"""

prices = {"coffee": 3.5, "bagel": 2.25, "muffin": 2.75, "tea": 3.0}

for item, price in prices.items(): # items() returns each key and value together as a tuple.
    print(f"{item}: ${price:.2f}")

for item in prices: # iterating over a dictionary directly gives only its keys.
    print(item)

print(f"${sum(prices.values()):.2f}") # values() returns only the values.