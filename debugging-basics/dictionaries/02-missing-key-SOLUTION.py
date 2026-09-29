"""
Objective: the code below should output the capital of country, or "unknown" if the country is not in capitals. It raises an error instead. Find the bug and fix it.
"""

capitals = {"France": "Paris", "Japan": "Tokyo", "Canada": "Ottawa"}

country = "Germany"

print(capitals.get(country, "unknown")) # looking up a missing key with square brackets raises a KeyError. get() returns a default instead.