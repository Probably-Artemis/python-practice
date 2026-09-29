"""
Objective: the code below should output "HELLO" with no spaces around it, but the output is wrong. Find the bug and fix it.
"""

messy = "   hello   "

messy = messy.strip().upper() # string methods return a new string rather than changing the original. the result was never saved.

print(messy)