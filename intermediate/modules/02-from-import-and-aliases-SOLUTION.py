"""
Objective: output the square root of 81 and the value of pi, importing sqrt and pi from math so they can be used without the math. prefix. Then import the statistics module under the shorter name stats, and use it to output the mean and median of grades.
Restriction: you may not edit preexisting code.
"""

grades = [88, 92, 75, 64, 99, 81]

import statistics as stats  # as imports a module under a different name, for clarity or resolving conflicts.
from math import (  # this imports only the names listed, and they're used without a prefix.
    pi,
    sqrt,
)

print(sqrt(81))
print(pi)

print(stats.mean(grades))
print(stats.median(grades)) # with an even number of items, the median is the average of the two middle values.

# from math import * would import every name in math at once. avoid it, since it makes it impossible to tell where a name came from.