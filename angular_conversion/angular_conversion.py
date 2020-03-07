# Angular conversion.

# Import math module.
import math

# Define function.
def header(title):
    # Print out a nice header.
    # params: str(title)
    # return: str(header)

    # Get the length of title.
    length = len(title)

    # Concatenate header string.
    header = "=" * length + "\n" + title.upper() + "\n" + "=" * length

    return header


# Print header.
print(header("Angular conversion"))

# User input.
while True:
    choice = input("Are you entering degrees or radians? (d/r) ").strip().lower()
    if choice == "d" or choice == "r":
        break
    else:
        continue


# If degrees.
if choice == "d":
    while True:
        try:
            degrees = float(input("Please enter degrees: ").strip())
            break
        except ValueError:
            print("Only numbers are accepted! Correct format: 180.00")
            continue

    # Convert degrees to radians.
    radians = math.radians(degrees)

    # Print result.
    print("%.2f degrees = %.2f radians" % (degrees, radians))


# If radians.
if choice == "r":
    while True:
        try:
            radians = float(input("Please enter radians: ").strip())
            break
        except ValueError:
            print("Only numbers are accepted! Correct format: 3.14")
            continue

    # Convert radians to degrees.
    degrees = math.degrees(radians)

    # Print result.
    print("%.2f radians = %.2f degrees" % (radians, degrees))


