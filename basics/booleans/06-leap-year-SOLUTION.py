"""
Objective: a year is a leap year if it is divisible by 4, except for years divisible by 100, which are only leap years if they are also divisible by 400. Using one boolean expression, output True if year is a leap year and False otherwise. Test your code with 2024 (leap), 1900 (not leap), 2000 (leap), and 2023 (not leap).
Restriction: you may not use if statements.
"""

year = 2024

is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) # the parentheses matter here. and happens before or, the same way * happens before +.

print(is_leap)