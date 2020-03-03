# Random Numbers Lab
# ------------------
# Write a program that uses a while loop to generate
# 100 random numbers between 1 and 10. After the program
# prints out all the random numbers output the sum of all
# the random numbers generated and the average of all the
# random numbers generated.

# Import random module.
import random

# Initialize variables.
i = 1
total = 0

# Start the while loop.
while i <= 100:

    # Generate a random number.
    number = random.randint(1, 10)

    # This is essentially the same:
    # number = random.randrange(1, 11)

    # Print result of current iteration.
    print("#{}: \t {}".format(i, number))

    # Update variables.
    i += 1
    total += number


# Print the sum and average of all numbers generated.
average = total / 100
print("The sum is:", total)
print("The average is:", average)
