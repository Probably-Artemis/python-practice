"""
Objective: a person can enter the concert if they have a ticket, are not banned, and are at least 13 years old. Output True if the person described below can enter, and False otherwise.
Restriction: you may not edit preexisting code, and you may not use if statements.
"""

has_ticket = True

is_banned = False

age = 16

can_enter = has_ticket and not is_banned and age >= 13 # and is only True when both sides are True. not flips True to False and back.

print(can_enter)

# there's no need to write has_ticket == True. has_ticket is already True or False on its own.