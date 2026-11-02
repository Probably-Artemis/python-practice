"""
Objective: using keyword arguments, call describe_pet so that it outputs "Biscuit is a 4 year old dog." Then call it again with the arguments in a different order and get the same output.
Restriction: you may not edit preexisting code.
"""

def describe_pet(name, species, age):
    print(f"{name} is a {age} year old {species}.")

describe_pet(name="Biscuit", species="dog", age=4) # keyword arguments are matched by name rather than by position.
describe_pet(age=4, name="Biscuit", species="dog")

# positional and keyword arguments can be mixed, as long as the positional ones come first: describe_pet("Biscuit", age=4, species="dog")