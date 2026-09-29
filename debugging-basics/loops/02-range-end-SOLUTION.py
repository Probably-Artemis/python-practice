"""
Objective: the code below should output the numbers 1 through 10, but the output is wrong. Find the bug and fix it.
"""

for i in range(1, 11): # range stops just before its second argument, so range(1, 10) ends at 9.
    print(i)