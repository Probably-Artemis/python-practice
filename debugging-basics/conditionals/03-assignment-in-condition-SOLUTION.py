"""
Objective: the code below should output "Access granted." if password is "swordfish", but it raises an error instead. Find the bug and fix it.
"""

password = "swordfish"

if password == "swordfish": # = cannot be used inside a condition, which raises a SyntaxError. == compares.
    print("Access granted.")