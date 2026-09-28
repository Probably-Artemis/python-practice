"""
Objective: output the result of 0.1 + 0.2. It will not be what you expect. Then output the same sum rounded to two decimal places. Finally, output the type of 10 / 5.
"""

print(0.1 + 0.2) # computers store floats in binary, and 0.1 can't be written exactly in binary, the same way 1/3 can't be written exactly in decimal.
print(round(0.1 + 0.2, 2)) # the second number tells round() how many decimal places to keep.
print(type(10 / 5)) # / always makes a float, even when the answer is a whole number like 2.0