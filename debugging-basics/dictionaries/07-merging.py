"""
Objective: the code below should combine the inventory of two stores into one dictionary, adding quantities together for items both stores carry, then output the combined inventory and store_a. store_a should be left unchanged. It runs, but the output is wrong. There are two bugs. Find them and fix them.
"""

store_a = {"apples": 10, "bread": 4, "eggs": 12}

store_b = {"bread": 6, "eggs": 24, "milk": 8}

combined = store_a

combined.update(store_b)

print(combined)
print(store_a)