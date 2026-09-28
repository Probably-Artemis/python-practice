"""
Objective: for every number from 1 to 100, output "Fizz" if it is divisible by 3, "Buzz" if it is divisible by 5, "FizzBuzz" if it is divisible by both, and the number itself otherwise.
"""

for n in range(1, 101):
    if n % 15 == 0: # a number divisible by both 3 and 5 is always divisible by 15.
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)