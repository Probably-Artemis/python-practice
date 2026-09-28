"""
Objective: output the numbers 1 through 10 using a for loop. Then, using a second for loop, output every even number from 2 to 20.
"""

for i in range(1, 11): # range stops just before the second number, so we need 11 to include 10.
    print(i)

for i in range(2, 21, 2): # the third number is the step, just like in slicing.
    print(i)