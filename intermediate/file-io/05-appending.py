"""
Objective: ask the user for a note and add it to the end of output/notes.txt, keeping any notes already there. Then output every note in the file, numbered. Run the file several times to make sure earlier notes are kept.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.