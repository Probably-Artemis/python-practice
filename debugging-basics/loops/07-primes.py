"""
Objective: the code below should output every prime number less than 30. It runs, but the output is wrong. There are two bugs. Find them and fix them.
"""

is_prime = True

for n in range(2, 30):
    for divisor in range(1, n):
        if n % divisor == 0:
            is_prime = False

    if is_prime:
        print(n)