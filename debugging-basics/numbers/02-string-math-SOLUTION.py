"""
Objective: the code below should output 15, but the output is wrong. Find the bug and fix it.
"""

a = "5"

b = "10"

print(int(a) + int(b)) # a and b are strings, so + concatenated them into "510". they must be cast to integers first.