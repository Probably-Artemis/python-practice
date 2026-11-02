"""
Objective: ask the user for two numbers and output the first divided by the second. If either input is not a number, output "please enter numbers only". If the second number is 0, output "cannot divide by zero". Neither case should produce an error.
Restriction: you may not use if statements.
"""

try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print(a / b)
except ValueError:
    print("please enter numbers only")
except ZeroDivisionError: # each except handles one kind of error. python uses the first one that matches.
    print("cannot divide by zero")