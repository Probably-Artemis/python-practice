"""
Objective: data/students.csv holds a header line, then one student per line, with a name and a grade separated by a comma. Without using the csv module, output each student's name and grade, like "alex: 90", then output the class average.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.

grades = []

with open(folder / "data" / "students.csv") as file:
    file.readline() # readline() reads a single line. reading the header here means the loop below starts at the first student.

    for line in file:
        name, grade = line.strip().split(",")
        grades.append(int(grade))
        print(f"{name}: {grade}")

print("Average:", sum(grades) / len(grades))

# splitting on commas breaks as soon as a value contains a comma itself, like "Smith, Sam". the csv module, used in 08, handles cases like that.