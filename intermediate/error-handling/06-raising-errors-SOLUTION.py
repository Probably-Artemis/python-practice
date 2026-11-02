"""
Objective: write a function named make_username that takes a name and returns it in lowercase with spaces replaced by underscores. If the name is empty, it should raise a ValueError with the message "name cannot be empty". If the name is longer than 20 characters, it should raise a ValueError with the message "name is too long". Call it with "John Doe", "", and "A Very Long Name Indeed Here", catching any error and outputting its message.
"""

def make_username(name):
    if name == "":
        raise ValueError("name cannot be empty") # raise creates an error on purpose. the code that called the function decides how to handle it.
    if len(name) > 20:
        raise ValueError("name is too long")
    return name.lower().replace(" ", "_")

for name in ["John Doe", "", "A Very Long Name Indeed Here"]:
    try:
        print(make_username(name))
    except ValueError as error: # as error stores the error itself, so its message can be output.
        print(error)