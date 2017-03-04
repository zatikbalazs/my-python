"""
Demonstration of packing and unpacking
arguments and keyword arguments.
"""

# Packing/unpacking arguments.
def add(*args):
    total = 0

    for arg in args:
        total += arg

    return total


numbers = [1, 2, 3, 4, 5]
result = add(*numbers)
print(result)


print()


# Packing/unpacking keyword arguments.
def show_ages(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


# Simple keyword arguments.
# show_ages(Tom = 20, Elizabeth = 43, Balázs = 31)

# Using a dictionary.
people = {"Jack": 20, "Zack": 25, "Mary": 33, "Zatik Balázs": 31}
show_ages(**people)
