"""
Objective: data/numbers.txt holds one whole number per line. Output how many numbers there are, their total, and their average.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.