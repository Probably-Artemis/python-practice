"""
Objective: using a for loop, count down from 10 to 1, then output "Liftoff!".
"""

for i in range(10, 0, -1): # counting down needs a negative step. the stop value is 0 so that 1 is the last number.
    print(i)

print("Liftoff!") # this isn't indented, so it runs once after the loop ends instead of every time through.