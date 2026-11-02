"""
Objective: write each item in groceries to output/groceries.txt, one item per line. Then open the file again, read it, and output its contents to prove it worked.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.

groceries = ["eggs", "milk", "bread", "coffee"]