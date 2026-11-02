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

# numbers and original are two names for the same list, the same trap as lists/12. changing the list through numbers changes it everywhere.

def doubled_copy(numbers):
    result = []
    for n in numbers:
        result.append(n * 2)
    return result

fresh = [1, 2, 3]
doubled = doubled_copy(fresh)

print(fresh)
print(doubled)