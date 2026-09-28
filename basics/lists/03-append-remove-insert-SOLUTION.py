"""
Objective: starting with an empty list, add "eggs", "milk", and "bread" to it one at a time. Then remove "milk", and add "coffee" to the very front. Output the list after every step.
"""

groceries = []

groceries.append("eggs") # append always adds to the end.
print(groceries)

groceries.append("milk")
print(groceries)

groceries.append("bread")
print(groceries)

groceries.remove("milk") # remove deletes the first matching item it finds, and errors if the item isn't there.
print(groceries)

groceries.insert(0, "coffee") # insert takes an index, then the item to put there. everything after it shifts over by one.
print(groceries)