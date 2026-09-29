"""
Objective: the code below should output the last food in foods, but it raises an error instead. Find the bug and fix it.
Restriction: your code must still work if items are added to or removed from foods.
"""

foods = ["pizza", "ramen", "tacos", "pancakes", "curry"]

print(foods[-1]) # a list of 5 items has indexes 0 through 4, so foods[5] raises an IndexError. -1 always refers to the last item.