# This script will print all prime numbers
# up to a user defined maximum value.

# Print header.
print("=" * 17)
print("ALL PRIME NUMBERS")
print("=" * 17)

while True:
    try:
        # User enters upper limit.
        max_number = int(input("Show all prime numbers up until this number: ").strip())

        if max_number < 2:
            print("There are no prime numbers smaller than " + str(max_number) + ".\n")

        else:
            # 2 is the first prime number and the only one that is even.
            print(2)

            # How many prime numbers found?
            found = 1

            # Start the sequence with 3.
            number = 3

            # Print all prime numbers until the limit specified by the user.
            while number <= max_number:

                # Initialize variable.
                is_prime = True

                # We won't divide by 0, 1 and the number itself.
                for i in range(2, number):

                    # Break the loop the first time the remainder is 0.
                    if number % i == 0:
                        is_prime = False
                        break

                if is_prime == True:
                    print(number)
                    found += 1

                number += 1

            # Success, print message and break out of main loop.
            print("RESULT: {} prime numbers found between 0 and {}.".format(found, max_number))
            break

    except ValueError:
        print("Please enter a number!\n")
