"""
Objective: unpack color into three variables named red, green, and blue, then output each one on its own line with a label, like "red: 255". Then swap the values of a and b and output both.
Restriction: you may not edit preexisting code, you may not use indexing, and you may not create a third variable to perform the swap.
"""

color = (255, 128, 0)

a = "first"

b = "second"

red, green, blue = color # the number of variables on the left must match the number of items in the tuple, or python raises a ValueError.

print("red:", red)
print("green:", green)
print("blue:", blue)

a, b = b, a # the right side is packed into a tuple before anything is assigned, so neither value is lost.

print(a, b)