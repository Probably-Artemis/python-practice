"""
Objective: the code below should output ['eggs', 'milk'], but the output is wrong. Find the bug and fix it.
"""

groceries = ["eggs"]

groceries.append("milk") # append() changes the list in place and returns None. assigning that result back replaced the list with None.

print(groceries)