"""
Objective: the code below should ask "What is your name? " and then output "Hello, <name>!". It runs, but the output is not quite right. There are two bugs. Find them and fix them.
"""

name = input("What is your name? ") # without the trailing space, the user's typing is squished against the question.

print("Hello, " + name + "!") # print() puts a space between each argument, which put a space before the exclamation point.