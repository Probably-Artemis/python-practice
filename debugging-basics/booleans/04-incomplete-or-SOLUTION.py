"""
Objective: the code below should output True if color is "red" or "green", and False otherwise. Since color is "blue", it should output False, but the output is wrong. Find the bug and fix it.
"""

color = "blue"

print(color == "red" or color == "green") # or does not repeat the comparison for you. the original was (color == "red") or ("green"). when the left side is False, or returns the right side, so it output "green".