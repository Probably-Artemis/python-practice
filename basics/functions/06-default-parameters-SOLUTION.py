"""
Objective: write a function named greet that takes a name and a greeting, and returns a string like "Hello, Sam!". If no greeting is given, it should default to "Hello". Output the result of calling it with and without a greeting.
"""

def greet(name, greeting="Hello"): # parameters with defaults must come after parameters without them.
    return greeting + ", " + name + "!"

print(greet("Sam"))
print(greet("Sam", "Good morning"))