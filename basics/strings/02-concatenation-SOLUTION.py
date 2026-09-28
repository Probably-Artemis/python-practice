"""
Objective: define two variables, each of the string type, then output them to the terminal on the same line. The variables should have no whitespace between them. Print the variables again, this time with a space between them.
"""

# the words "foo" and "bar" are often used as generic placeholders.
# they are derived from the acronym FUBAR, which a lot of code in fact is.
a = "foo"
b = "bar"

print(a + b) # print variables with no whitespace between them

print(a, b) # print variables with whitespace between them

print(a + " " + b) # this also works to print with whitespace between them, but is less polished.