"""
Objective: using one list comprehension each, build a list of the even numbers in numbers, then a list of the numbers greater than 10, then a list of the even numbers greater than 10. Output all three.
Restriction: you may not edit preexisting code.
"""

numbers = [3, 8, 15, 22, 7, 10, 41, 6, 18]

evens = [n for n in numbers if n % 2 == 0] # an if at the end keeps only the items where the condition is True.
big = [n for n in numbers if n > 10]
big_evens = [n for n in numbers if n % 2 == 0 and n > 10]

print(evens)
print(big)
print(big_evens)