"""
Objective: data/inventory.csv holds a header line, then an item, price, and quantity on each line. Using the csv module, output the name of every item with fewer than 5 in stock, then the total value of all stock (price times quantity, added up across every item). Finally, write output/restock.csv with the columns item and needed, holding one row for each item with fewer than 5 in stock, where needed is how many more it takes to reach 10.
Restriction: you may not edit preexisting code.
"""

from pathlib import Path

folder = Path(__file__).parent # the folder this file is in, so the data and output folders can be found no matter where python is run from.

import csv

low = []
total = 0

with open(folder / "data" / "inventory.csv", newline="") as file: # the csv module asks for newline="" so it can handle line endings itself.
    for row in csv.DictReader(file): # DictReader uses the header line as keys, so each row is a dictionary.
        quantity = int(row["quantity"])
        total += float(row["price"]) * quantity

        if quantity < 5:
            print(row["item"])
            low.append((row["item"], 10 - quantity))

print(f"${total:.2f}")

with open(folder / "output" / "restock.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["item", "needed"])
    writer.writerows(low) # writerows() writes one row per item in the list.