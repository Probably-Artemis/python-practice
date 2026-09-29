"""
Objective: products maps a product code to a dictionary of details. Output the name of every product with fewer than 10 in stock. Then output the total value of all stock (price times quantity, added up across every product).
Restriction: you may not edit preexisting code, and your code must still work if products are added or removed.
"""

products = {
    "A100": {"name": "notebook", "price": 2.5, "stock": 40},
    "A200": {"name": "pen", "price": 1.25, "stock": 6},
    "B100": {"name": "backpack", "price": 35.0, "stock": 3},
    "B200": {"name": "lamp", "price": 18.0, "stock": 12}
}

for code, details in products.items():
    if details["stock"] < 10:
        print(details["name"])

total = 0

for details in products.values(): # the codes aren't needed here, so values() is enough.
    total += details["price"] * details["stock"]

print(f"${total:.2f}")