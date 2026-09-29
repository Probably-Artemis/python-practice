"""
Objective: the code below should output the numbers 1 through 5, but it never stops. Find the bug and fix it. Press ctrl+c in the terminal to stop the program.
"""

count = 1

while count <= 5:
    print(count)
    count += 1 # count was never changed, so count <= 5 stayed True forever.