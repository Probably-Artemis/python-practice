"""
Objective: ask the user for an item name, its price, and how many they are buying. Output a receipt showing the subtotal, a 6.25% sales tax, and the total. All money should show exactly two decimal places.
"""

item = input("Item: ")
price = float(input("Price: "))
quantity = int(input("Quantity: ")) # you can't buy half a sweater, so int makes sense here.

subtotal = price * quantity
tax = subtotal * 0.0625 # 6.25% as a decimal.
total = subtotal + tax

print(f"{quantity} x {item}")
print(f"Subtotal: ${subtotal:.2f}") # :.2f shows a float with exactly two decimal places. round() would turn 5.10 into 5.1, which looks odd for money.
print(f"Tax:      ${tax:.2f}")
print(f"Total:    ${total:.2f}")