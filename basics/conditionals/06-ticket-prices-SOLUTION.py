"""
Objective: movie tickets cost $12. Children under 12 and seniors 65 or older pay $8 instead. On Tuesdays, everyone gets $2 off. Ask the user for their age and the day of the week, then output their ticket price.
"""

age = int(input("Age: "))
day = input("Day of the week: ")

if age < 12 or age >= 65:
    price = 8
else:
    price = 12

if day.lower() == "tuesday": # lower() means "Tuesday", "tuesday", and "TUESDAY" all count.
    price -= 2

print("Your ticket costs $" + str(price))

# the two if statements are separate on purpose. the Tuesday discount applies no matter which price was picked above.