"""
the module for 09-main-guard-SOLUTION.py.
"""

def greet(name):
    return "Hello, " + name + "!"

if __name__ == "__main__": # python sets __name__ to "__main__" only in the file that was run directly. in an imported file, it holds the module's name instead.
    print("testing greet...")
    print(greet("test"))