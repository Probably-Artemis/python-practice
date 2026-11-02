"""
Objective: output five rolls of a six-sided die, making sure the same five rolls come out every time the file is run.
"""

import random

random.seed(61) # random numbers in python are not truly random. they come from a formula, and the seed is its starting point, so the same seed always produces the same sequence.

for i in range(5):
    print(random.randint(1, 6))

# seeds are useful for testing, where the same input should always produce the same output. never use random for passwords or anything security related. the secrets module exists for that.