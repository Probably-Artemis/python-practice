"""
Objective: ask the user for a note and add it to the end of output/notes.txt, keeping any notes already there. Then output every note in the file, numbered. Run the file several times to make sure earlier notes are kept.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.

path = folder / "output" / "notes.txt"

note = input("Note: ")

with open(path, "a") as file: # "a" opens the file for appending. new writes go at the end, and nothing already there is erased.
    file.write(note + "\n")

with open(path) as file:
    number = 1
    for line in file:
        print(f"{number}. {line.rstrip()}")
        number += 1