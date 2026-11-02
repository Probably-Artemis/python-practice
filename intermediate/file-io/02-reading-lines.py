"""
Objective: output each line of data/poem.txt with its line number in front, like "1: Shall I compare thee to a summer's day?". There should be no blank lines between them.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.