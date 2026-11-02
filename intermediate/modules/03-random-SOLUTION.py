"""
Objective: using the random module, output a roll of a six-sided die, a random color from colors, and a random decimal number between 0 and 1. Run the file a few times to see the results change.
Restriction: you may not edit preexisting code.
"""

colors = ["red", "green", "blue", "yellow"]

import random

print(random.randint(1, 6)) # unlike range, randint includes both ends.
print(random.choice(colors))
print(random.random()) # 0 is possible, 1 is not.