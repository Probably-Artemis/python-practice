"""
Objective: using the variable full_name, output the person's initials in uppercase followed by periods (for "ada lovelace", output "A.L."). Then output the name as last name, a comma, then first name, each capitalized (for "ada lovelace", output "Lovelace, Ada").
Restriction: you may not edit preexisting code, and you may not use split(). Your code must still work for any first and last name separated by a single space.
"""

full_name = "ada lovelace"

space = full_name.find(" ") # everything before the space is the first name, and everything after it is the last name.
first = full_name[:space]
last = full_name[space + 1:] # the + 1 skips over the space itself.

print(first[0].upper() + "." + last[0].upper() + ".")
print(last.capitalize() + ", " + first.capitalize())