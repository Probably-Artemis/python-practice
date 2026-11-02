"""
Objective: using one list comprehension, flatten grid into a single list of numbers and output it. Then, using another, build a list of every (x, y) pair where x and y are each 0, 1, or 2, but are not equal to each other, and output that.
Restriction: you may not edit preexisting code.
"""

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat = [n for row in grid for n in row] # the for clauses run in the same order they would as nested loops: for row in grid, then for n in row.
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]

print(flat)
print(pairs)