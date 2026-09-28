"""
Objective: the variable below is a mess. Output it in all uppercase, then in all lowercase, then with the extra spaces removed from the beginning and end.
Restriction: you may not edit preexisting code.
"""

messy = "   pYtHoN iS fUn   "

print(messy.upper())
print(messy.lower())
print(messy.strip()) # strip() removes whitespace from both ends. lstrip() and rstrip() only do one side each.

# string methods hand back a new string rather than changing the original, so messy is still a mess down here.
print(messy.strip().capitalize()) # methods can also be chained together, running left to right.