"""
Roulette Statistics
===================
Get statistics of hundreds or thousands
of spins on the roulette wheel.
"""

# Import modules.
import random

# Create a list of numbers on roulette wheel (0-36).
numbers = [number for number in range(37)]

# How many spins?
spins = int(input("How many spins? ").strip())

# Start spins.
for spin in range(spins):
    spin_num = spin + 1
    hit = random.choice(numbers)
    print("{}. spin: {}".format(spin_num, hit))

# Statistics.
print("=" * 10)
print("Statistics".upper())
print("=" * 10)
print("Spins: {}".format(spin_num))
