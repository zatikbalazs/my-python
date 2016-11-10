def collatz(number):
    """
    Function for the "Collatz Sequence".
    It receives a positive integer number.
    It returns a positive integer number.
    """
    # Even number given.
    if number % 2 == 0:
        new_number = number // 2

    # Odd number given.
    else:
        new_number = (3 * number) + 1

    # Print and return new number.
    print(new_number)
    return new_number

# Intro text.
print("The simplest impossible math problem! (Collatz Sequence)")
print("No matter what number you enter, the sequence will always result in 1!")

while True:
    try:
        # Get a number from user.
        number = int(input("\nPlease enter a number: ").strip())

        ## Only accept positive integer numbers.
        if number > 0:
            # Call the collatz() function until it returns 1.
            while number != 1:
                number = collatz(number)

            # When we get to number 1.
            if number == 1:
                print("See, I told you so. :)")
                break
        else:
            print("Only positive integer numbers are accepted.")

    except ValueError:
        print("Sorry, only numbers are accepted.")
