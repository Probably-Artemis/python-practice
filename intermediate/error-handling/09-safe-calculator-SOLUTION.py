"""
Objective: write a calculator that keeps asking the user for a calculation like "8 / 2", with spaces around the operator, until they type "quit". It should support +, -, *, and /, and output each result. A calculation that is not three parts, numbers that are not numbers, an unknown operator, and division by zero should each output a helpful message instead of producing an error.
"""

def calculate(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b # a ZeroDivisionError raised here is caught by the try block in the loop below.
    raise ValueError(f"unknown operator {operator}")

while True:
    line = input("Calculation: ").strip()

    if line == "quit":
        break

    parts = line.split()

    if len(parts) != 3:
        print("please use the format: number operator number")
        continue

    try:
        a = float(parts[0])
        b = float(parts[2])
    except ValueError:
        print("both sides must be numbers")
        continue

    try:
        print(calculate(a, parts[1], b))
    except ZeroDivisionError:
        print("cannot divide by zero")
    except ValueError as error:
        print(error)