"""
Objective: keep asking the user for the password until they type it correctly. Once they do, output "Access granted." along with how many attempts it took.
Restriction: you may not edit preexisting code.
"""

stored_password = "hunter2"

attempts = 1
attempt = input("Password: ")

while attempt != stored_password: # as we must continue indefinitely, a while loop is proper.
    print("Wrong password.")
    attempts += 1
    attempt = input("Password: ")

print("Access granted. It took", attempts, "attempts.")