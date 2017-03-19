# Hypotenuse of a right-angled triangle.

# Import math module.
import math

# Define function.
def header(title):
    """
    Prints out a nice header.
    params: str(title)
    return: str(header)
    """
    # Get the length of title.
    length = len(title)

    # Concatenate header string.
    header = "=" * length + "\n" + title.upper() + "\n" + "=" * length

    return header


# Print header.
print(header("Hypotenuse calculator"))

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
print("The length of the hypotenuse is: %.2f" % (c))
