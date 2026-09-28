"""
Objective: grid is a list of lists, where each inner list is one row. Output the grid as three rows of numbers separated by spaces, then output the number in the very center, then the total of every number in the grid.
Restriction: you may not edit preexisting code, and you may not use sum().
"""

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
    for number in row:
        print(number, end=" ") # end=" " puts a space after each number instead of starting a new line.
    print() # an empty print ends the row.

print(grid[1][1]) # the first index picks the row, and the second picks the item within that row.

total = 0

for row in grid:
    for number in row:
        total += number

print(total)