# Hypotenuse of a right-angled triangle.

# Import math module.
import math

# User input.
while True:
    try:
        a = float(input("Please enter the length of side A: ").strip())
        break
    except ValueError:
        print("Only numbers are accepted! Correct format: 12.50")
        continue

while True:
    try:
        b = float(input("Please enter the length of side B: ").strip())
        break
    except ValueError:
        print("Only numbers are accepted! Correct format: 12.50")
        continue

# Calculate hypotenuse.
c = math.hypot(a, b)

# Print result.
print("The length of the hypotenuse (side C) is: %.2f" % (c))
