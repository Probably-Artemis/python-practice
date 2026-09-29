"""
Objective: the code below should build a 3 by 3 grid of zeros, set only the top left item to 1, and output the grid. It runs, but the output is wrong. Find the bug and fix it.
"""

grid = [[0, 0, 0] for row in range(3)] # * 3 repeated the same inner list three times rather than making three separate lists, so changing one row changed them all.

grid[0][0] = 1

print(grid)