"""
Objective: write a shopping list program. Keep asking the user for a command until they quit. "add" should ask for an item and add it to the list. "remove" should ask for an item and remove it, or say it isn't on the list. "show" should output every item, numbered, or say the list is empty. "quit" should end the program. Any other command should output a helpful message.
"""

shopping = []

while True: # this loop runs forever until a break inside it ends it.
    command = input("Command (add, remove, show, quit): ").strip().lower()

    if command == "add":
        item = input("Item to add: ")
        shopping.append(item)
    elif command == "remove":
        item = input("Item to remove: ")
        if item in shopping: # checking first keeps remove() from erroring on an item that isn't there.
            shopping.remove(item)
        else:
            print(item, "isn't on the list.")
    elif command == "show":
        if len(shopping) == 0:
            print("The list is empty.")
        for number, item in enumerate(shopping, start=1):
            print(f"{number}. {item}")
    elif command == "quit":
        print("Goodbye!")
        break
    else:
        print("Unknown command. Try add, remove, show, or quit.")