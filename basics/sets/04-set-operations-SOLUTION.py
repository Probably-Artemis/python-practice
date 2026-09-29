"""
Objective: output the hobbies alex and sam have in common, then every hobby either of them has, then the hobbies only alex has, then the hobbies only one of them has. Output each result in alphabetical order.
Restriction: you may not edit preexisting code, and you may not use loops.
"""

alex = {"chess", "hiking", "painting", "cooking"}

sam = {"hiking", "running", "cooking", "reading"}

print(sorted(alex & sam)) # intersection. only items in both sets.
print(sorted(alex | sam)) # union. items in either set.
print(sorted(alex - sam)) # difference. items in alex that are not in sam.
print(sorted(alex ^ sam)) # symmetric difference. items in exactly one of the two sets.

# sorted() returns a list, which is why the output uses square brackets.
# each operator also has a method form: alex.intersection(sam), alex.union(sam), alex.difference(sam), and alex.symmetric_difference(sam).