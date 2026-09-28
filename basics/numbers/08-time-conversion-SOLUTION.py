"""
Objective: total_seconds holds an amount of time in seconds. Output it in the format "X days, X hours, X minutes, X seconds".
Restriction: you may not edit preexisting code, and your code must still work if the value of total_seconds is changed.
"""

total_seconds = 100000

days = total_seconds // 86400 # 60 seconds * 60 minutes * 24 hours = 86400 seconds in a day.
leftover = total_seconds % 86400 # whatever didn't fit into a full day.

hours = leftover // 3600
leftover = leftover % 3600

minutes = leftover // 60
seconds = leftover % 60

print(days, "days,", hours, "hours,", minutes, "minutes,", seconds, "seconds")