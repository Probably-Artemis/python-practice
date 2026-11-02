"""
Objective: write a function named is_even that returns True if a number is even and False otherwise, and a function named is_leap that does the same for leap years. Then, using is_even, output every even number from 1 to 10, and using is_leap, output every leap year from 1896 to 1912.
Restriction: neither function may contain an if statement.
"""

def is_even(n):
    return n % 2 == 0 # a comparison already produces True or False, so it can be returned directly.

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

for n in range(1, 11):
    if is_even(n):
        print(n)

for year in range(1896, 1913):
    if is_leap(year):
        print(year)

# 1900 is missing from the output on purpose. it is divisible by 100 but not by 400.