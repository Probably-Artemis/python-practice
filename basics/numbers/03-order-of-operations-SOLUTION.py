"""
Objective: each line below outputs the wrong number. Add parentheses so the first line outputs 20, the second outputs 8, and the third outputs 64.
Restriction: you may not add, remove, or reorder any numbers or operators. Parentheses only.
"""

print((2 + 3) * 4) # multiplication normally happens before addition, so the original was 2 + (3 * 4).
print(10 - (4 - 2)) # subtraction goes left to right, so the original was (10 - 4) - 2.
print((2 ** 3) ** 2) # exponents are the odd one out and go right to left, so the original was 2 ** (3 ** 2), which is 512.