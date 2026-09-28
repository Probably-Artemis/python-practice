"""
Objective: output the largest of a, b, and c.
Restriction: you may not edit preexisting code, and you may not use max(). Your code must still work if the values are changed, including when two of them are equal.
"""

a = 14

b = 29

c = 7

if a >= b and a >= c: # >= rather than > so that ties still get handled.
    print(a)
elif b >= c: # if we get here, a isn't the largest, so it's down to b and c.
    print(b)
else:
    print(c)