"""
Objective: ask the user for two numbers and an operator (+, -, *, or /), then output the result. If the user tries to divide by zero, output "cannot divide by zero" instead of producing an error. If the operator is not one of the four, output "unknown operator".
"""

a = float(input("First number: "))
operator = input("Operator (+, -, *, /): ")
b = float(input("Second number: "))

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b == 0: # checking before dividing means the division never runs with a zero.
        print("cannot divide by zero")
    else:
        print(a / b)
else:
    print("unknown operator")