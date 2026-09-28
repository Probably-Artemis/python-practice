"""
Objective: using each of the operators +=, -=, *=, and //= at least once, change score so that it ends up equal to 7. Output score after every step.
Restriction: you may not edit preexisting code, and you may not give score a new value with a plain =.
"""

score = 10

score += 5 # same as score = score + 5. score is now 15
print(score)

score *= 2 # 30
print(score)

score -= 2 # 28
print(score)

score //= 4 # 7
print(score)