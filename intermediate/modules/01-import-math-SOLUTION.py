"""
Objective: using the math module, output the square root of 144, pi rounded to 5 decimal places, 4.1 rounded up to the nearest whole number, and 4.9 rounded down to the nearest whole number.
"""

import math # imports normally go at the top of a file. in later files here, they come after any provided code, so that code stays untouched.

print(math.sqrt(144))
print(round(math.pi, 5))
print(math.ceil(4.1))
print(math.floor(4.9)) # the module name goes in front of everything it provides, so it's clear where each function came from.