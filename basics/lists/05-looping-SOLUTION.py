"""
Objective: output each item in tasks on its own line, numbered starting from 1, like "1. laundry".
Restriction: you may not edit preexisting code, and your code must still work if items are added to or removed from tasks.
"""

tasks = ["laundry", "homework", "dishes", "call mom"]

number = 1

for task in tasks: # a for loop over a list hands you each item in order.
    print(str(number) + ". " + task)
    number += 1