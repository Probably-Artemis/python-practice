"""
Objective: the code below should output "even" if number is even and "odd" if it is odd, but it raises an error instead. Find the bug and fix it.
"""

number = 13

if number % 2 == 0:
    print("even") # python uses indentation to know which lines belong to the if. without it, an IndentationError is raised.
else:
    print("odd")