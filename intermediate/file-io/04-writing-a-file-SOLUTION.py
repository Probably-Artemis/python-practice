"""
Objective: write each item in groceries to output/groceries.txt, one item per line. Then open the file again, read it, and output its contents to prove it worked.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.

groceries = ["eggs", "milk", "bread", "coffee"]

path = folder / "output" / "groceries.txt"

with open(path, "w") as file: # "w" opens the file for writing. it creates the file if it doesn't exist, and erases it first if it does.
    for item in groceries:
        file.write(item + "\n") # write() does not add a newline on its own.

with open(path) as file: # with no mode given, a file is opened for reading.
    print(file.read(), end="")