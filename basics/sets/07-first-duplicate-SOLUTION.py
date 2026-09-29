"""
Objective: output the first number in numbers that appears for a second time. If no number repeats, output "no duplicates".
Restriction: you may not edit preexisting code, you may not use count(), and you may only iterate over numbers once.
"""

numbers = [4, 9, 2, 7, 9, 4, 2]

seen = set()
duplicate = None

for n in numbers:
    if n in seen: # if we've seen n before, this is its second appearance.
        duplicate = n
        break
    seen.add(n)

if duplicate is None:
    print("no duplicates")
else:
    print(duplicate)

# 9 is the answer rather than 4, since the second 9 comes before the second 4.