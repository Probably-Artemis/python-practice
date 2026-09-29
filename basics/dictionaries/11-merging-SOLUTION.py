"""
Objective: two stores are combining their inventory. Build a single dictionary holding every item from both stores, where items carried by both stores have their quantities added together. Output the result.
Restriction: you may not edit preexisting code, and neither store_a nor store_b may be changed.
"""

store_a = {"apples": 10, "bread": 4, "eggs": 12}

store_b = {"bread": 6, "eggs": 24, "milk": 8}

combined = store_a.copy() # copying first means store_a is left unchanged.

for item, quantity in store_b.items():
    combined[item] = combined.get(item, 0) + quantity

print(combined)

# store_a | store_b also merges two dictionaries, but for shared keys it keeps the value from store_b instead of adding them.