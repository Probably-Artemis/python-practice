"""
Objective: ask the user for a height, then output a right triangle of asterisks that many rows tall. For a height of 4, it should look like:
*
**
***
****
Then output the same triangle upside down.
Restriction: you may not multiply strings (such as "*" * 4). Use a loop inside a loop instead.
"""

height = int(input("Height: "))

for row in range(1, height + 1):
    line = ""
    for star in range(row): # the inner loop runs once per star, and each row gets one more star than the last.
        line += "*"
    print(line)

for row in range(height, 0, -1): # same idea, but counting rows down instead of up.
    line = ""
    for star in range(row):
        line += "*"
    print(line)