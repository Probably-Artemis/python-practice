"""
Objective: the code below should remove "urgent" from tags if it is there, and do nothing if it isn't, then output tags. It raises an error instead. Find the bug and fix it.
"""

tags = {"work", "later"}

tags.remove("urgent")

print(sorted(tags))