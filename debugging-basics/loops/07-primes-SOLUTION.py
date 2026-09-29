"""
Objective: the code below should output every prime number less than 30. It runs, but the output is wrong. There are two bugs. Find them and fix them.
"""

for n in range(2, 30):
    is_prime = True # this was set once before the outer loop, so after the first non-prime, it stayed False for every number after.

    for divisor in range(2, n): # every number is divisible by 1, so starting at 1 marked every number as not prime.
        if n % divisor == 0:
            is_prime = False

    if is_prime:
        print(n)