"""
Objective: write a contact book program that stores names and phone numbers. Keep asking the user for a command until they quit. "add" should ask for a name and number and save them. "find" should ask for a name and output the number, or say the contact doesn't exist. "delete" should ask for a name and remove that contact, or say it doesn't exist. "list" should output every contact in alphabetical order by name, or say the book is empty. "quit" should end the program. Any other command should output a helpful message.
"""

contacts = {}

while True:
    command = input("Command (add, find, delete, list, quit): ").strip().lower()

    if command == "add":
        name = input("Name: ")
        number = input("Number: ") # phone numbers are stored as strings, since they can hold dashes and leading zeros.
        contacts[name] = number
    elif command == "find":
        name = input("Name: ")
        if name in contacts:
            print(contacts[name])
        else:
            print(name, "is not in the contact book.")
    elif command == "delete":
        name = input("Name: ")
        if name in contacts:
            del contacts[name]
        else:
            print(name, "is not in the contact book.")
    elif command == "list":
        if len(contacts) == 0:
            print("The contact book is empty.")
        for name in sorted(contacts): # sorted() on a dictionary returns a sorted list of its keys.
            print(f"{name}: {contacts[name]}")
    elif command == "quit":
        break
    else:
        print("Unknown command. Try add, find, delete, list, or quit.")