"""
Objective: using a list comprehension, build a list of the squares of the numbers 1 through 10 and output it. Then do the same for the cubes.
Restriction: each list must be built in a single line.
"""

squares = [n ** 2 for n in range(1, 11)] # read it as "n squared, for every n in range(1, 11)."
cubes = [n ** 3 for n in range(1, 11)]

print(squares)
print(cubes)

# the same list as a regular loop:
# squares = []
# for n in range(1, 11):
#     squares.append(n ** 2)