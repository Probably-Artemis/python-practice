"""
Objective: add_item should add an item to a list and return the list, starting a new empty list whenever no list is given. Run the code below and notice that chores contains an item that belongs in groceries. Fix add_item so that each call without a list starts with an empty one.
Restriction: you may only edit add_item.
"""

def add_item(item, items=[]):
    items.append(item)
    return items

groceries = add_item("eggs")
chores = add_item("laundry")

print(groceries)
print(chores)