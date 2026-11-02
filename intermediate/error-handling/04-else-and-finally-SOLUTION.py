"""
Objective: ask the user for a number. If it is not a number, output "not a number". If it is, output its square. Either way, output "done" at the very end. Use else and finally to do this.
Restriction: the try block may only contain the line that converts the input.
"""

try:
    number = float(input("Number: "))
except ValueError:
    print("not a number")
else: # else runs only if the try block raised no error.
    print(number ** 2)
finally: # finally always runs, error or not. it is normally used for cleanup, like closing a connection.
    print("done")

# keeping the try block small means the except only catches errors from the line you expect to fail, rather than hiding bugs elsewhere.