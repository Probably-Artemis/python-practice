"""
Objective: ask the user for three side lengths. If they can't form a triangle, output "not a triangle". Otherwise, output whether the triangle is "equilateral" (all sides equal), "isosceles" (exactly two sides equal), or "scalene" (no sides equal). Three sides form a triangle only if every pair of sides adds up to more than the remaining side.
"""

a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

if a + b > c and a + c > b and b + c > a: # this check also rules out zero and negative sides, since those can never pass all three.
    if a == b == c: # we nest this if statement so we know we no longer have to deal with potential non-triangles.
        print("equilateral")
    elif a == b or b == c or a == c:
        print("isosceles")
    else:
        print("scalene")
else:
    print("not a triangle")