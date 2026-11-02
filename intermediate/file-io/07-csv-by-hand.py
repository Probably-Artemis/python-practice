"""
Objective: data/students.csv holds a header line, then one student per line, with a name and a grade separated by a comma. Without using the csv module, output each student's name and grade, like "alex: 90", then output the class average.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.