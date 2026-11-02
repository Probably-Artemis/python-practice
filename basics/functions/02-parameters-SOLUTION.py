"""
Objective: write a function named greet that takes a name and outputs "Hello, <name>!". Then write a function named rectangle_area that takes a width and a height and outputs the area. Call each one at least twice with different arguments.
"""

def greet(name): # name is a parameter. it holds whatever value is passed in when the function is called.
    print("Hello, " + name + "!")

def rectangle_area(width, height):
    print(width * height)

greet("Sam")
greet("Alex")

rectangle_area(3, 4) # arguments are matched to parameters by position, so width is 3 and height is 4.
rectangle_area(10, 2.5)