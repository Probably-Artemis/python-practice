"""
Objective: output the sum of a and b as a number (the answer should be 42, not 1230). Then output c as a whole number.
Restriction: you may not edit preexisting code.
"""

a = "12"

b = "30"

c = 3.99

print(int(a) + int(b)) # adding two strings concatenates them together. converting them to int first makes + perform addition instead.
print(int(c)) # int() chops off the decimal rather than rounding, so 3.99 becomes 3. use round() if you want 4.