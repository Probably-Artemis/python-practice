"""
Objective: in this folder, create a new file named conversions.py holding two functions: to_celsius, which converts Fahrenheit to Celsius, and to_fahrenheit, which converts Celsius to Fahrenheit. Then, in this file, import your conversions module and use it to output 212 F in Celsius and 100 C in Fahrenheit.
"""

import conversions_SOLUTION as conversions  # the provided solution module is named conversions_SOLUTION.py. in your own work, this would just be import conversions, or whatever you named the module.

print(conversions.to_celsius(212))
print(conversions.to_fahrenheit(100))

# any .py file can be imported as a module, using its name without the .py. python looks for it in the same folder as the file being run.