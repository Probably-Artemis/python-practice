"""
Objective: the code below should output 15, but it raises an error instead. Leave a comment explaining why, then fix it.
Restriction: you may not use the global keyword.
"""

# total only exists inside add_shipping. a variable created inside a function is local to it and disappears once the function returns, so print(total) raised a NameError.
def add_shipping(price):
    total = price + 5
    return total

total = add_shipping(10) # this total is a separate variable outside the function. the two share a name and nothing else.

print(total)

# global would also make this work, but it lets a function change a variable used anywhere in the program, which makes bugs much harder to track down. returning values is the standard way.