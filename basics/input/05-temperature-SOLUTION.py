"""
Objective: ask the user for a temperature in Fahrenheit, then output it in Celsius, rounded to one decimal place. The formula is C = (F - 32) * 5 / 9.
"""

fahrenheit = float(input("Temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print(round(celsius, 1), "degrees Celsius")