# Define functions.
def header(title):
    # Print out a nice header.
    # params: str(title)
    # return: str(header)

    # Get the length of title.
    length = len(title)

    # Concatenate header string.
    header = "=" * length + "\n" + title.upper() + "\n" + "=" * length

    return header

def show_factors(number):
    # Show factors of the given number.
    # params: int(number)
    # return: list(factors)

    # Create list for factor pairs.
    factors = ["1, " + str(number)]

    # Create list to check if factor pair has been added or not.
    pair_totals = []

    # We won't divide by 0, 1 and the number itself.
    for i in range(2, number):

        # Check if remainder is 0 and make sure not to repeat factor pairs.
        if number % i == 0 and i + (number / i) not in pair_totals:

            factors.append(str(i) + ", " + str(int(number / i)))
            pair_totals.append(i + (number / i))

    return factors


# Start execution.
print(header("Show factors of number!"))

while True:
    try:
        # User enters number.
        number = int(input("Get the factors of: ").strip())

        # Validate user input.
        if number < 1:
            print("Number must be bigger than 0.\n")
            continue

        # Call function.
        factors = show_factors(number)

        # Print result.
        for item in factors:
            print(item)

        # Done. Break out of main loop.
        break

    except ValueError:
        print("Only numbers please!\n")
