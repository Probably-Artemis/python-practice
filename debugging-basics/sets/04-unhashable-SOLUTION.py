"""
Objective: the code below should store each point in visited only once, then output how many unique points were visited, which is 2. It raises an error instead. Find the bug and fix it.
"""

visited = set()

visited.add((0, 0)) # sets can only hold immutable values. a list is mutable, which raises a TypeError, but a tuple works.
visited.add((1, 2))
visited.add((0, 0))

print(len(visited))