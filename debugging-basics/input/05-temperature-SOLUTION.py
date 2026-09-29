"""
Objective: the code below should ask for a temperature in Fahrenheit, then output it in Celsius rounded to one decimal place. Entering 98.6 should output 37.0, but the output is wrong. There are two bugs. Find them and fix them.
"""

fahrenheit = float(input("Temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9 # without parentheses, 32 * 5 / 9 happened before the subtraction.

print(round(celsius, 1)) # the 1 was outside round(), so it was printed as its own value instead of setting the decimal places.