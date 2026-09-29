"""
Objective: the code below should output True, since 0.1 + 0.2 is 0.3, but the output is wrong. Find the bug and fix it.
"""

print(abs((0.1 + 0.2) - 0.3) < 0.000001) # 0.1 + 0.2 is actually 0.30000000000000004, so == fails. floats should be compared by checking whether they are close enough.

# math.isclose(0.1 + 0.2, 0.3) does the same thing.