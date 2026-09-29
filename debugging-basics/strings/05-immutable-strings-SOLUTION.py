"""
Objective: the code below should output "Hello", but it raises an error instead. Find the bug and fix it.
"""

word = "hello"

word = "H" + word[1:] # strings are immutable, so assigning to word[0] raises a TypeError. we must build a new string instead.

print(word)