"""
Objective: ask the user for two numbers, which may have decimals, then output their sum, difference, product, and quotient.
"""

a = float(input("First number: ")) # float rather than int, since the user might type something like 2.5
b = float(input("Second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b) # if the second number is 0, this line errors. the conditionals folder covers how to guard against that.