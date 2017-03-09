# How to use the ternary operator in Python.
# ("do this" if True else "do that")

# User input.
age = int(input("How old are you? ").strip())

# Use the ternary operator to display text according to the data given.
print("You are allowed to drive a car." if age >= 18 else "You are not allowed to drive a car.")

# Use the ternary operator to assign value to a variable.
old_enough = True if age >= 18 else False

print(old_enough)
