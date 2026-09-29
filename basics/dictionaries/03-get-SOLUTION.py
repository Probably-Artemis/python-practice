"""
Objective: ask the user for a country, then output its capital. If the country is not in capitals, output "unknown" instead.
Restriction: you may not edit preexisting code, and you may not use if statements.
"""

capitals = {"France": "Paris", "Japan": "Tokyo", "Canada": "Ottawa", "Kenya": "Nairobi", "Peru": "Lima"}

country = input("Country: ")

print(capitals.get(country, "unknown")) # capitals[country] raises a KeyError for a missing key. get() returns the second argument instead.