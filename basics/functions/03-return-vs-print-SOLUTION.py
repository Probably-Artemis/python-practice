"""
Objective: the code below should output 25, but it raises an error instead. Change square so that it works.
Restriction: you may only edit the body of square.
"""

def square(n):
    return n * n # print() only shows a value. return hands it back to the caller, where it can be stored or used in math.

total = square(3) + square(4)

print(total)

# with print() instead of return, square returned None, and None + None raises a TypeError.