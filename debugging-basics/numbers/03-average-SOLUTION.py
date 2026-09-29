"""
Objective: the code below should output the average of a, b, and c, which is 8.0, but the output is wrong. Find the bug and fix it.
"""

a = 4

b = 8

c = 12

average = (a + b + c) / 3 # division happens before addition, so only c was being divided by 3.

print(average)