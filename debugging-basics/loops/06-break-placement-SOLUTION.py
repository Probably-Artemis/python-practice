"""
Objective: the code below should output the first number from 1 to 100 that is divisible by both 7 and 11, which is 77, but the output is wrong. Find the bug and fix it.
"""

for n in range(1, 101):
    if n % 7 == 0 and n % 11 == 0:
        print(n)
        break # break was indented to the level of the loop rather than the if, so the loop exited during its first iteration.