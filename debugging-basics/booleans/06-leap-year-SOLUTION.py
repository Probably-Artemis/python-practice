"""
Objective: a year is a leap year if it is divisible by 4, except for years divisible by 100, which are only leap years if they are also divisible by 400. The code below should output whether year is a leap year. 1900 is not a leap year, but the output is wrong. Find the bug and fix it. Test your fix with 2024 (leap), 1900 (not leap), 2000 (leap), and 2023 (not leap).
"""

year = 1900

is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) # and and or were swapped, and without parentheses, and is evaluated before or.

print(is_leap)