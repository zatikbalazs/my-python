"""
Lists Vs Tuples
---------------
1. A list is a mutable data type.
   A tuple is an IMMUTABLE data type.
   Tuples are basically immutable lists (sequences).
   A tuple's values and the order of values cannot be changed.

2. Lists are created with hard brackets [].
   Tuples are created with parentheses ().
"""

# List.
cars = ["Mercedes", "Volvo", "Ford", "Honda"]
print(len(cars))

# Tuple.
numbers = (1, 2, 3, 4, 5)
print(len(numbers))

# Get values.
print(cars[2])
print(numbers[1:3])

# Assign values.
# Lists are mutable. Its values can be changed.
cars[0] = "Mercedes-Benz"
# Tuples are immutable! Its values CANNOT BE CHANGED!
# numbers[1] = 20

# Transform list into tuple.
print(type(cars))
cars = tuple(cars)
print(type(cars))

# Transform tuple into list.
print(type(cars))
cars = list(cars)
print(type(cars))

# Get max and min values.
print(max(cars))
print(min(cars))
print(max(numbers))
print(min(numbers))
