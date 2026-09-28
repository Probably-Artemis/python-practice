"""
Objective: ask the user for a password. If it matches the stored password, output "Access granted." Otherwise, output "Access denied."
Restriction: you may not edit preexisting code.
"""

stored_password = "hunter2"

attempt = input("Password: ")

if attempt == stored_password:
    print("Access granted.")
else:
    print("Access denied.")

# real software never stores passwords in plain text like this. they get hashed first, but that's not my job.