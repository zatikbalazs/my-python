# Import modules.
import random

# Print header.
print("=" * 24)
print("LOTTERY NUMBER GENERATOR")
print("=" * 24)

while True:
    # We only accept numbers from user input.
    try:
        # COLLECT DATA AND VALIDATE USER INPUT.
        # How many numbers.
        how_many = int(input("How many numbers do you need? ").strip())

        # Validate user input.
        if how_many < 1:
            print("Error: Entered number must be bigger than 0!\n")
            continue

        # Smallest possible number.
        min_num = int(input("Enter the smallest possible number: ").strip())

        # Validate user input.
        if min_num < 0:
            print("Error: Entered number must be bigger than or equal to 0!\n")
            continue

        # Biggest possible number.
        max_num = int(input("Enter the biggest possible number: ").strip())

        # Validate user input.
        if max_num < 1:
            print("Error: Entered number must be bigger than 0!\n")
            continue

        # We need enough "room" to pick the winning numbers from.
        if how_many > max_num - min_num + 1:
            print("Error: Program needs a bigger min-max range to choose the numbers from!\n")
            continue

        # USER INPUT VALID, GENERATE THE WINNING NUMBERS!
        # Create empty list of winning numbers.
        winning_numbers = []

        # Generate winning numbers.
        while len(winning_numbers) < how_many:

            # Generate random number.
            number = random.randint(min_num, max_num)

            # List can only contain unique numbers.
            if number not in winning_numbers:
                winning_numbers.append(number)

        # Sort winning numbers.
        winning_numbers.sort()

        # Print winning numbers.
        print()
        print("*" * 25)
        print("Your winning numbers are:")
        for number in winning_numbers:
            print(number, end=" ")
        print()
        print("*" * 25)

        # Success! Break out of loop.
        break

    except ValueError:
        print("Error: Invalid input! Only numbers please.\n")
        continue
