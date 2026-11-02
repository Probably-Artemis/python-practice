"""
Objective: using the datetime module, output how many days apart January 1, 2026 and December 25, 2026 are. Then output the day of the week that January 1, 2000 fell on, as a word.
"""

from datetime import date

start = date(2026, 1, 1) # year, month, day.
end = date(2026, 12, 25)

print((end - start).days) # subtracting two dates gives a timedelta, which holds the difference between them.

print(date(2000, 1, 1).strftime("%A")) # strftime() formats a date as text. %A means the full name of the weekday.