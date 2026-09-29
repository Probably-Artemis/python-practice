"""
Objective: the code below should output "foo bar", but the output is wrong. Find the bug and fix it.
"""

first = "foo"

last = "bar"

print(first + " " + last) # + adds nothing between the strings it joins, so the space must be added by hand. print(first, last) also works.