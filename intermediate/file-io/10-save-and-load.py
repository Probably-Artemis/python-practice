"""
Objective: write a to-do list program that remembers its tasks between runs, by saving them to output/todo.txt, one per line. When it starts, it should load any saved tasks. Then it should keep asking for a command until the user quits. "add" should ask for a task and add it. "done" should ask for a task number and remove that task. "show" should output every task, numbered. "quit" should save the tasks and end the program. Write separate functions for loading and saving. intermediate/error-handling covers what you need for the first run, when there is no saved file yet.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.