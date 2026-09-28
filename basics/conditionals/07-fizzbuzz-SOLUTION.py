"""
Objective: if n is divisible by 3, output "Fizz". If it is divisible by 5, output "Buzz". If it is divisible by both, output "FizzBuzz". Otherwise, output n itself. Test your code with 9, 10, 15, and 7.
Restriction: your code must still work if the value of n is changed.
"""

n = 15

if n % 3 == 0 and n % 5 == 0: # this check has to come first. if it came after the % 3 check, 15 would output "Fizz" and stop there.
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)