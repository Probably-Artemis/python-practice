"""
Objective: run the code below and notice that original changes, even though double_all never mentions it by name. Leave a comment explaining why. Then write a function named doubled_copy that returns a new list with every number doubled, leaving the list passed to it unchanged. Use it on a new list, and output both lists to prove it.
Restriction: you may not edit preexisting code.
"""

def double_all(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2

original = [1, 2, 3]

double_all(original)

print(original)