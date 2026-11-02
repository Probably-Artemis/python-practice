"""
Objective: write a function named factorial that returns the factorial of n (n! is n * (n - 1) * ... * 1, and 0! is 1). Then write a function named count_down that outputs the numbers from n down to 1, followed by "Liftoff!". Output factorial(5), then call count_down(5).
Restriction: you may not use loops. Each function must call itself instead.
"""

def factorial(n):
    if n == 0: # the base case. without it, the function would keep calling itself until python raises a RecursionError.
        return 1
    return n * factorial(n - 1) # each call works on a smaller value than the last, until it reaches the base case.

def count_down(n):
    if n == 0:
        print("Liftoff!")
        return
    print(n)
    count_down(n - 1)

print(factorial(5))
count_down(5)

# anything written with recursion can also be written with a loop. recursion tends to read better for problems that contain smaller copies of themselves, like folders inside folders.