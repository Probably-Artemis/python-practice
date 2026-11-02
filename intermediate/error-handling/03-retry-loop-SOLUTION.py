"""
Objective: write a function named get_int that takes a prompt, keeps asking the user until they enter a whole number, and then returns it. Each invalid entry should output "try again". Use get_int to ask for two numbers, then output their sum.
"""

def get_int(prompt):
    while True:
        try:
            return int(input(prompt)) # if int() succeeds, return exits both the loop and the function.
        except ValueError:
            print("try again")

a = get_int("First number: ")
b = get_int("Second number: ")

print(a + b)