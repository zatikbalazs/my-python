# Import random module.
import random

# Set health variable.
health = random.randint(1, 50)
# Set level of difficulty.
difficulty = 1

# Show current health of user.
print("Your current health is at {}%".format(health))

# Offer a health potion to the user.
drink = input("Would you like to drink a health potion? (y/n) ").strip().lower()

# What did the user do?
if drink == "y" or drink == "yes":
    while True:
        # Set potion strength and increase user's health.
        potion_strength = int(random.randint(25, 50) / difficulty)
        health += potion_strength
        # Health cannot be more than 100.
        if health >= 100:
            print("Your health is now at 100%. Go and enjoy your life!")
            break
        else:
            print("Drinking the potion increased your health to {}%".format(health))
            # Offer another health potion.
            drink = input("Would you like to drink another health potion? (y/n) ").strip().lower()
            if drink == "y" or drink == "yes":
                continue
            else:
                print("Alright buddy, see you next time!")
                break
else:
    print("I'm sorry I couldn't help you. Bye-bye!")
