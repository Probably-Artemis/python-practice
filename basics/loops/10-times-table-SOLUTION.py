"""
Objective: output a multiplication table for the numbers 1 through 9, with the numbers lined up in neat columns.
"""

for row in range(1, 10):
    line = ""
    for col in range(1, 10):
        line += f"{row * col:4}" # :4 pads each number out to 4 characters wide, which keeps the columns lined up.
    print(line)