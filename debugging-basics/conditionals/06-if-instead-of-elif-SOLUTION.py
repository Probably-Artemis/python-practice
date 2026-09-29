"""
Objective: the code below should output only one word describing temperature: "hot" above 80, "warm" above 60, and "cold" otherwise. A temperature of 85 should output only "hot", but the output is wrong. Find the bug and fix it.
"""

temperature = 85

if temperature > 80:
    print("hot")
elif temperature > 60: # a second if starts a new, separate check, so 85 passed both. elif only runs when everything above it was False.
    print("warm")
else:
    print("cold")