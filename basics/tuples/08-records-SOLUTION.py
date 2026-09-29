"""
Objective: each tuple in cart holds an item name, its price, and the quantity being bought. For each item, output a line like "apple: 10 x $0.50 = $5.00". Then output the total cost of the cart.
Restriction: you may not edit preexisting code, and your code must still work if items are added to or removed from cart.
"""

cart = [
    ("apple", 0.5, 10),
    ("bread", 3.25, 2),
    ("milk", 4.0, 1)
]

total = 0

for name, price, quantity in cart:
    cost = price * quantity
    total += cost
    print(f"{name}: {quantity} x ${price:.2f} = ${cost:.2f}")

print(f"Total: ${total:.2f}")

# tuples are a good fit for records like these, where every entry has the same fixed layout.