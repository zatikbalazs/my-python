# List of VIP guests.
vip_guests = ["Schwarzenegger", "Stallone", "Statham", "Rourke", "Van-damme", "Segal", "Norris"]

while True:
    # Ask guest for his name.
    name = input("\nHello sir, what is your name? ").strip().capitalize()

    # If he is on the list.
    if name in vip_guests:
        print("Welcome back Mr. {}!".format(name))

        # Ask if he wants to be removed from the list.
        remove = input("Would you like to be removed from the list? (y/n) ").strip().lower()

        if remove == "y" or remove == "yes":
            vip_guests.remove(name)
            print("You have been removed from the list.")
        else:
            print("I'm glad you decided to stay. :)")

    # If he is not on the list.
    else:
        print("Sorry, your name is not on the list.")

        # Ask if he wants to be added to the list.
        add = input("Mr. {}, would you like to be added to the list? (y/n) ".format(name)).strip().lower()

        if add == "y" or add == "yes":
            vip_guests.append(name)
            print("You have been added to the list. Welcome!")
        else:
            print("No problem. Have a good night!")
