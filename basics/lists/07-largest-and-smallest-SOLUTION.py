"""
Objective: output the largest and smallest numbers in temps.
Restriction: you may not edit preexisting code, and you may not use max(), min(), or any kind of sorting. Your code must still work if temps is changed, including if every number is negative.
"""

temps = [41, 38, 55, 29, 60, 47, 33]

largest = temps[0] # start with the first item rather than 0. if every temp were negative, starting at 0 would give the wrong answer.
smallest = temps[0]

for temp in temps:
    if temp > largest:
        largest = temp
    if temp < smallest: # a separate if, not an elif, since the first item can be both the largest and smallest so far.
        smallest = temp

print("Largest:", largest)
print("Smallest:", smallest)