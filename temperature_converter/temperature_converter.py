# Coding Exercise: Functions
#
# Write a function that will convert either a Celsius temperature
# to a Fahrenheit temperature or a Fahrenheit temperature to Celsius.

def header(title):
    # Create a nice header.
    # params: str(title)
    # return: str(header)

    # Get the length of title.
    length = len(title)

    # Concatenate header string.
    header = "=" * length + "\n" + title.upper() + "\n" + "=" * length

    return header


def convert_temp(unit, temp):
    # Convert either a Celsius temperature to a Fahrenheit
    # temperature or a Fahrenheit temperature to Celsius.
    # params: str(unit), float(temp)
    # return: float(result)

    # Calculate result.
    if unit == "C":
        result = (temp * 1.8) + 32
    elif unit == "F":
        result = (temp - 32) / 1.8

    return result


# Print header.
print(header("Temperature Converter"))

# User input.
while True:
    unit = input("Celsius or Fahrenheit (C/F)? ").strip().upper()

    if unit == "C":
        target_unit = "F"
        break
    elif unit == "F":
        target_unit = "C"
        break
    else:
        print("Invalid unit: \"{}\"".format(unit))
        continue

while True:
    try:
        temp = float(input("Enter temperature: ").strip())
        break
    except ValueError:
        print("Only numbers are accepted! Correct format: 25.00")
        continue

# Call the converter function.
result = convert_temp(unit, temp)

# Print the rounded result.
print("{} {} = {} {}".format(temp, unit, round(result, 2), target_unit))
