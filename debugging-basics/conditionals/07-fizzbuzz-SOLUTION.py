"""
Objective: the code below should output "Fizz" if n is divisible by 3, "Buzz" if it is divisible by 5, "FizzBuzz" if it is divisible by both, and n itself otherwise. When n is 15 it should output FizzBuzz, but the output is wrong. Find the bug and fix it. Test your fix with 9, 10, 15, and 7.
"""

n = 15

if n % 3 == 0 and n % 5 == 0: # the most specific check must come first. before, any multiple of 15 stopped at the % 3 check.
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)