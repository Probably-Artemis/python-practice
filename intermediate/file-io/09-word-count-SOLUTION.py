"""
Objective: for data/excerpt.txt, output the number of lines, words, and characters in the file, then the three most common words and how many times each appears, listing any tied words in the order they first appear. Capitalization and the punctuation at the ends of words should be ignored.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.

from collections import Counter # covered in modules/06.

with open(folder / "data" / "excerpt.txt") as file:
    text = file.read()

lines = text.splitlines()
words = [w.strip('.,;:?"').lower() for w in text.split()] # strip() removes any of the given characters from both ends, including the quotation marks around dialogue.

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(text)) # this count includes spaces and newline characters.

for word, count in Counter(words).most_common(3): # most_common() keeps tied words in the order they were first counted.
    print(word, count)