"""
Objective: output the second item in planets. Then replace the third item with "Earth" and output the whole list.
Restriction: you may not edit preexisting code.
"""

planets = ["Mercury", "Venus", "Pluto", "Mars"]

print(planets[1])

planets[2] = "Earth" # unlike strings, lists are mutable.
print(planets)