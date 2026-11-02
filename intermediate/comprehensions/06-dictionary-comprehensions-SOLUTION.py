"""
Objective: using a dictionary comprehension, build a dictionary mapping each word in words to its length, and output it. Then, using a second one, build a copy of prices with every price 10% lower, rounded to two decimal places, keeping only items that originally cost more than 3. Output that as well.
Restriction: you may not edit preexisting code.
"""

words = ["apple", "banana", "kiwi"]

prices = {"coffee": 3.5, "bagel": 2.25, "sandwich": 7.0, "tea": 3.0}

lengths = {w: len(w) for w in words} # curly braces and a key: value pair at the front make a dictionary instead of a list.
sale = {item: round(price * 0.9, 2) for item, price in prices.items() if price > 3}

print(lengths)
print(sale)