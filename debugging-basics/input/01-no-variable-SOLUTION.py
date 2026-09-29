"""
Objective: the code below should ask the user for their name, then greet them with "Hello, <name>!", but it raises an error instead. Find the bug and fix it.
"""

name = input("What is your name? ") # the input was never stored in a variable, so name did not exist and a NameError was raised.

print("Hello, " + name + "!")