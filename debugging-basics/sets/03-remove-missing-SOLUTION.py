"""
Objective: the code below should remove "urgent" from tags if it is there, and do nothing if it isn't, then output tags. It raises an error instead. Find the bug and fix it.
"""

tags = {"work", "later"}

tags.discard("urgent") # remove() raises a KeyError when the item is missing. discard() does nothing instead.

print(sorted(tags))