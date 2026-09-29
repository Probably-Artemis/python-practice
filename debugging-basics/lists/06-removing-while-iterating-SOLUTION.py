"""
Objective: the code below should remove every even number from numbers and output [5, 9], but the output is wrong. Find the bug and fix it.
"""

numbers = [2, 4, 5, 6, 8, 9]

for n in numbers[:]: # removing items shifts everything after them left by one, so the loop skipped the item right after each removal. iterating over a copy avoids that.
    if n % 2 == 0:
        numbers.remove(n)

print(numbers)