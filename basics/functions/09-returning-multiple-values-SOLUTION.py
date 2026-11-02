"""
Objective: write a function named min_max that takes a list of numbers and returns both the smallest and largest number. Unpack the result into two variables and output them.
Restriction: you may not edit preexisting code, and you may not use min(), max(), or any kind of sorting.
"""

temps = [41, 38, 55, 29, 60, 47, 33]

def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]

    for n in numbers:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n

    return smallest, largest # this returns a single tuple holding both values.

low, high = min_max(temps)

print("Lowest:", low)
print("Highest:", high)