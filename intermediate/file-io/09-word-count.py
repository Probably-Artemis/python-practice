"""
Objective: for data/excerpt.txt, output the number of lines, words, and characters in the file, then the three most common words and how many times each appears, listing any tied words in the order they first appear. Capitalization and the punctuation at the ends of words should be ignored.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.