# Create a dictionary.
birthdays = {"Mom": "July 2",
             "Dad": "October 25",
             "Wife": "January 21",
             "Brother": "June 26",
             "Sister": "February 23"}

while True:
    # User input.
    print("Enter a name: (blank to quit)")
    name = input().strip().capitalize()

    # Quit program if input is blank.
    if name == "":
        break

    # If name is found, print birthday.
    if name in birthdays:
        print("{} is the birthday of {}.\n".format(birthdays[name], name))

    # If name is not found, update database.
    else:
        print("I do not have birthday information for {}.".format(name))
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.\n")
