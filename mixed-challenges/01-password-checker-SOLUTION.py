"""
Objective: keep asking the user for a new password until they enter a strong one. A strong password is at least 8 characters long, has at least one digit, at least one uppercase letter, at least one lowercase letter, and no spaces. After each weak password, output every rule it broke, one per line. Once they enter a strong one, output "Strong password!" and how many tries it took.
"""

tries = 0
strong = False

while not strong:
    password = input("New password: ")
    tries += 1

    has_digit = False
    has_upper = False
    has_lower = False
    for ch in password:
        if ch.isdigit():
            has_digit = True
        elif ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True

    problems = []
    if len(password) < 8:
        problems.append("must be at least 8 characters")
    if not has_digit: # separate ifs, not elifs, so every broken rule gets reported.
        problems.append("needs a digit")
    if not has_upper:
        problems.append("needs an uppercase letter")
    if not has_lower:
        problems.append("needs a lowercase letter")
    if " " in password:
        problems.append("can't contain spaces")

    if len(problems) == 0:
        strong = True
    else:
        for problem in problems:
            print(problem)

print(f"Strong password! It took {tries} tries.")

# any() makes the checks shorter, if you've seen it: has_digit = any(ch.isdigit() for ch in password)