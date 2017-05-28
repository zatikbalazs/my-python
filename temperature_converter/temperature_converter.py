"""
Coding Exercise: Functions

Write a function that will convert either a Celsius temperature
to a Fahrenheit temperature or a Fahrenheit temperature to Celsius.

You'll need to have your function receive two parameters.
You might want to make the first parameter the temperature
to convert, and the second temperature a boolean indicating
whether the value sent is Celsius or Fahrenheit.
"""

def header(title):
    """
    Create a nice header.
    params: str(title)
    return: str(header)
    """
    # Get the length of title.
    length = len(title)

    # Concatenate header string.
    header = "=" * length + "\n" + title.upper() + "\n" + "=" * length

    return header


def convert_temp(temp, celsius):
    """
    Convert either a Celsius temperature to a Fahrenheit
    temperature or a Fahrenheit temperature to Celsius.
    params: float(temp), bool(celsius)
    return: float(result)
    """


# Print header.
print(header("Temperature Converter"))

# User input.
while True:
    try:
        temp = float(input("Enter temperature: ").strip())
        break
    except ValueError:
        print("Only numbers are accepted! Correct format: 25.00")
        continue
