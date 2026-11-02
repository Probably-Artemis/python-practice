"""
Objective: using any() and all() with generator expressions, output whether password contains at least one digit, whether it contains at least one uppercase letter, and whether every character in it is a letter or digit. Then, using sum() with a generator expression, output the sum of the squares of the numbers 1 through 100.
Restriction: you may not edit preexisting code, and you may not write any loops outside of the generator expressions.
"""

password = "Password123"

print(any(ch.isdigit() for ch in password)) # any() returns True as soon as one item is True.
print(any(ch.isupper() for ch in password))
print(all(ch.isalnum() for ch in password)) # all() returns False as soon as one item is False.

print(sum(n ** 2 for n in range(1, 101)))

# a generator expression looks like a list comprehension without the square brackets. it hands out one item at a time instead of building the whole list first, which saves memory.