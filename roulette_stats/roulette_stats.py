# Roulette Statistics
# ===================
# Get statistics of hundreds or thousands
# of spins on the roulette wheel.

# Import modules.
import random

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
hit_type = None

# Start spins.
for spin in range(spins):

    # Current number of spin.
    spin_num = spin + 1

    # Get random hit.
    hit = random.choice(numbers)

    # Even, odd or zero?
    if hit == 0:
        zero_hits += 1
        hit_type = "NULL"
    elif hit % 2 == 0:
        even_hits += 1
        deviation += 1
        hit_type = "EVEN"
    else:
        odd_hits += 1
        deviation -= 1
        hit_type = "ODD"

    # Display result of current spin.
    print("{}. hit: {},\t{}\tdeviation: {}".format(spin_num, hit, hit_type, deviation))

# Calculate percentages.
even_percentage = round((even_hits / spins) * 100, 2)
odd_percentage  = round((odd_hits / spins) * 100, 2)
zero_percentage = round((zero_hits / spins) * 100, 2)

# Display statistics.
print("-" * 10)
print("Statistics".upper())
print("-" * 10)
print("Spins:     {}\t(100% of 100%)".format(spins))
print("Even hits: {}\t({}% of 48.65%)".format(even_hits, even_percentage))
print("Odd hits:  {}\t({}% of 48.65%)".format(odd_hits, odd_percentage))
print("Zero hits: {}\t({}% of 2.70%)".format(zero_hits, zero_percentage))
