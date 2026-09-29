"""
Objective: the code below should remove every even number from numbers and output [5, 9], but the output is wrong. Find the bug and fix it.
"""

numbers = [2, 4, 5, 6, 8, 9]

for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)

print(numbers)