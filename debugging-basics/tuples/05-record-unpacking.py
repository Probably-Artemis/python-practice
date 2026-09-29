"""
Objective: each tuple in cart holds an item name, its price, and the quantity being bought. The code below should output the total cost of the cart, which is $15.50, but it raises an error instead. There are two bugs. Find them and fix them.
"""

cart = [
    ("apple", 0.5, 10),
    ("bread", 3.25, 2),
    ("milk", 4.0, 1)
]

total = 0

for name, price in cart:
    total += price

print(f"Total: ${total:.2f}")