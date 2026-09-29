"""
Objective: the code below should output True if answer is "yes", no matter how it is capitalized. It runs, but the output is wrong. Find the bug and fix it.
Restriction: you may not edit the line that creates answer.
"""

answer = "Yes"

print(answer.lower() == "yes") # string comparisons are case-sensitive, so "Yes" and "yes" are not equal.