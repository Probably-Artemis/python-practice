"""
Objective: output the entire contents of data/poem.txt.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.

with open(folder / "data" / "poem.txt") as file: # with closes the file automatically once the block ends, even if an error happens inside it.
    contents = file.read() # read() returns the whole file as one string.

print(contents, end="") # the file already ends with a newline, so end="" stops print() from adding a second one.