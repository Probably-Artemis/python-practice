"""
Objective: ask the user for the name of a file in the data folder, such as poem.txt, and output its contents. If the file does not exist, output "file not found" instead of producing an error. intermediate/error-handling covers the tools for this.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.

name = input("File name: ")

try:
    with open(folder / "data" / name) as file:
        print(file.read(), end="")
except FileNotFoundError: # opening a file that doesn't exist for reading raises a FileNotFoundError.
    print("file not found")