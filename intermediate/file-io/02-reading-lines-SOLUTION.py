"""
Objective: output each line of data/poem.txt with its line number in front, like "1: Shall I compare thee to a summer's day?". There should be no blank lines between them.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.

with open(folder / "data" / "poem.txt") as file:
    number = 1
    for line in file: # iterating over a file gives one line at a time, each still ending with its newline character.
        print(f"{number}: {line.rstrip()}") # rstrip() removes that newline, so print() doesn't add a blank line after it.
        number += 1