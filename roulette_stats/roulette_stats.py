"""
Roulette Statistics
===================
Get statistics of hundreds or thousands
of spins on the roulette wheel.
"""

# Import modules.
import random

# Define functions.
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
print(header("Roulette Stats"))

# Create a list of numbers on roulette wheel (0-36).
numbers = [number for number in range(37)]

# How many spins?
spins = int(input("How many spins? ").strip())

# Initialize variables for stats.
even_hits = 0
zero_hits = 0
odd_hits  = 0
deviation = 0

# Start spins.
for spin in range(spins):

    # Current number of spin.
    spin_num = spin + 1

    # Get random hit.
    hit = random.choice(numbers)

    # Even, odd or zero?
    if hit == 0:
        zero_hits += 1
    elif hit % 2 == 0:
        even_hits += 1
        deviation += 1
    else:
        odd_hits += 1
        deviation -= 1

    # Display result of current spin.
    print("{}. hit: {}, deviation: {}".format(spin_num, hit, deviation))

# Display statistics.
print("=" * 10)
print("Statistics".upper())
print("=" * 10)
print("Spins:     {}".format(spins))
print("Even hits: {}".format(even_hits))
print("Odd hits:  {}".format(odd_hits))
print("Zero hits: {}".format(zero_hits))
