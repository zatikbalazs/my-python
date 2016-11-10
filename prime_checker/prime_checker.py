# Define functions.
def header(title):
    """
    Prints out a nice header.
    args: str title
    return: str header
    """
    # Get the length of title.
    length = len(title)

    # Concatenate header string.
    header = "=" * length + "\n" + title.upper() + "\n" + "=" * length

    return header

def check_prime(number):
    """
    Checks if the given number is a prime number.
    args: int number
    return: bool is_prime, str evidence
    """
    # Initialize variables.
    is_prime = True
    evidence = None

    # We won't divide by 0, 1 and the number itself.
    for i in range(2, number):

        # Break the loop the first time the remainder is 0.
        if number % i == 0:

            # If the remainder is 0, then number is NOT a prime.
            is_prime = False

            # Save the last division as evidence.
            result = int(number / i)
            evidence = "{} / {} = {}".format(number, i, result)

            break

    return is_prime, evidence


# Start execution.
print(header("Is it a prime number?"))

while True:
    try:
        # User enters number.
        number = int(input("Please enter a number: ").strip())

        # Validate user input.
        if number < 2:
            print("{} is NOT a prime number.".format(number))
            break

        # Check prime number.
        is_prime, evidence = check_prime(number)

        if is_prime:
            print("{} is a prime number.".format(number))
        else:
            print("{} is NOT a prime number.".format(number))
            print(evidence)

        # Done. Break out of main loop.
        break

    except ValueError:
        print("Only numbers please!\n")
