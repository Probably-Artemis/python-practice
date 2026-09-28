"""
Objective: ask the user for their name, then greet them with "Hello, <name>!".
"""

name = input("What is your name? ") # the text inside input() is shown to the user as a prompt. the trailing space keeps their typing from being squished against the question. alternatively, one may use \n or \t to have the user answer on a second line, or after a greater length of whitespace respectively.

print("Hello, " + name + "!") # print("Hello,", name, "!") would put a space before the exclamation point.