"""
Objective: write a to-do list program that remembers its tasks between runs, by saving them to output/todo.txt, one per line. When it starts, it should load any saved tasks. Then it should keep asking for a command until the user quits. "add" should ask for a task and add it. "done" should ask for a task number and remove that task. "show" should output every task, numbered. "quit" should save the tasks and end the program. Write separate functions for loading and saving. intermediate/error-handling covers what you need for the first run, when there is no saved file yet.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.

path = folder / "output" / "todo.txt"

def load_tasks(path):
    try:
        with open(path) as file:
            return [line.rstrip("\n") for line in file]
    except FileNotFoundError: # the first time the program runs, there is no saved file yet.
        return []

def save_tasks(path, tasks):
    with open(path, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if len(tasks) == 0:
        print("Nothing to do.")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

tasks = load_tasks(path)

while True:
    command = input("Command (add, done, show, quit): ").strip().lower()

    if command == "add":
        tasks.append(input("Task: "))
    elif command == "done":
        try:
            number = int(input("Task number: "))
        except ValueError:
            number = 0 # 0 is never a valid task number, so the check below rejects it.

        if 1 <= number <= len(tasks): # checking the range matters. pop(-1) would quietly remove the last task instead of raising an error.
            tasks.pop(number - 1) # pop() removes the item at an index. the displayed numbers start at 1, so we subtract 1.
        else:
            print("That is not a task number.")
    elif command == "show":
        show_tasks(tasks)
    elif command == "quit":
        save_tasks(path, tasks)
        break
    else:
        print("Unknown command. Try add, done, show, or quit.")

# for saving more complicated data, like a list of dictionaries, the json module turns python data into text and back.