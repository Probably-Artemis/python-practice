"""
Objective: output every prime number less than 100. A prime number is a whole number greater than 1 that can only be divided evenly by 1 and itself.
"""

for n in range(2, 100):
    is_prime = True

    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break # one divisor is enough to prove n isn't prime, so there's no need to keep checking.

    if is_prime:
        print(n)

# this checks more divisors than it needs to. you only have to go up to the square root of n. try making it faster.