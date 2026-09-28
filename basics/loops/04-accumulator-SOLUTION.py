"""
Objective: using a loop, add up every whole number from 1 to 100 and output the total.
Restriction: you may not use sum().
"""

total = 0 # the total has to start at zero, and it has to start outside the loop. inside, it would reset every time through.

for i in range(1, 101):
    total += i

print(total)