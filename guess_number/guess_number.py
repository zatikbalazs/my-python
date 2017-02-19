# The "Guess The Number" game.

# Import module.
import random

# Define function.
def header(title):
    """
    Prints out a nice header.
    args: str(title)
    return: str(header)
    """
    # Get the length of title.
    length = len(title)

    # Concatenate header string.
    header = "=" * length + "\n" + title.upper() + "\n" + "=" * length

    return header


# Print header.
print(header("Guess the number game"))

# Computer thinks of a number.
secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

# User has 4 chances to guess the number.
for guesses_taken in range(1, 5):
    chances_left = 4 - guesses_taken
    try:
        guess = int(input("Please take a guess: ").strip())

        if guess < secret_number:
            print("Your guess is too low. (" + str(chances_left) + " chances left)")
        elif guess > secret_number:
            print("Your guess is too high. (" + str(chances_left) + " chances left)")
        else:
            break
    except ValueError:
        print("Invalid guess. You just wasted a chance.")

if guess == secret_number:
    print("\nCongratulations! You have found the secret number.")
else:
    print("\nSorry, the secret number was " + str(secret_number) + ".")
