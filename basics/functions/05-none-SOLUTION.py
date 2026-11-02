"""
Objective: write a function named find_index that takes a list and an item, and returns the index of the first time the item appears in the list. If the item is not in the list, it should return None. Using your function, output where "red", "green", and "purple" appear in colors, or "not found" for any that don't.
Restriction: you may not edit preexisting code, you may not use index(), and you may not check whether the item is in the list with in.
"""

colors = ["red", "green", "blue", "green"]

def find_index(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i # return exits the function immediately, so later matches are never reached.
    return None # a function that ends without a return statement returns None anyway, but writing it out makes the intent clear.

for target in ["red", "green", "purple"]:
    result = find_index(colors, target)

    if result is None: # None is a value meaning "nothing". is None is the standard way to check for it.
        print(target, "not found")
    else:
        print(target, "is at index", result)

# if not result would be wrong here. 0 is a valid index, but it counts as False, so "red" would be reported as not found.