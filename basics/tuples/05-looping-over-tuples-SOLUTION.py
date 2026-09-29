"""
Objective: points is a list of (x, y) tuples. For each point, output its distance from the origin (0, 0). The distance is the square root of x squared plus y squared.
Restriction: you may not edit preexisting code, and you may not use indexing.
"""

points = [(0, 0), (3, 4), (6, 8), (5, 12)]

for x, y in points: # each tuple is unpacked as the loop iterates over it.
    distance = (x ** 2 + y ** 2) ** 0.5 # raising a number to the power of 0.5 is the same as taking its square root.
    print(distance)