"""
Objective: the code below should output only one word describing temperature: "hot" above 80, "warm" above 60, and "cold" otherwise. A temperature of 85 should output only "hot", but the output is wrong. Find the bug and fix it.
"""

temperature = 85

if temperature > 80:
    print("hot")
if temperature > 60:
    print("warm")
else:
    print("cold")