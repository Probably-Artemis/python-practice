"""
Objective: using only math, output the ones digit of number, then the tens digit, then the sum of all four digits.
Restriction: you may not edit preexisting code, and you may not convert number to a string.
"""

number = 4731

ones = number % 10 # the remainder after dividing by 10 is always the last digit.
tens = number // 10 % 10 # floor dividing by 10 chops off the last digit, then % 10 grabs the new last digit.
hundreds = number // 100 % 10
thousands = number // 1000

print(ones)
print(tens)
print(ones + tens + hundreds + thousands)