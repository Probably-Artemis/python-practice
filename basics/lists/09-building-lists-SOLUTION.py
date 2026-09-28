"""
Objective: using a loop, build a list of the squares of the numbers 1 through 10 and output it. Then build a second list holding only the even numbers from numbers and output that.
Restriction: you may not edit preexisting code.
"""

numbers = [3, 8, 15, 22, 7, 10, 41, 6]

squares = []

for i in range(1, 11):
    squares.append(i ** 2)

print(squares)

evens = []

for n in numbers:
    if n % 2 == 0:
        evens.append(n)

print(evens)

# python has a shortcut for building lists like these, called a list comprehension:
# squares = [i ** 2 for i in range(1, 11)]
# evens = [n for n in numbers if n % 2 == 0]