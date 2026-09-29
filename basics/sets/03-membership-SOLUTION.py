"""
Objective: ask the user for a file name, such as "photo.PNG". If the file's extension is in allowed, output "accepted". Otherwise, output "rejected".
Restriction: you may not edit preexisting code, and capitalization of the extension should not matter.
"""

allowed = {"jpg", "png", "gif"}

filename = input("File name: ")

extension = filename.split(".")[-1].lower() # [-1] takes whatever comes after the last period, so "my.photo.png" still works.

if extension in allowed: # checking membership in a set is much faster than in a list, since python does not have to look at every item.
    print("accepted")
else:
    print("rejected")