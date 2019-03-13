# Create a dictionary.
birthdays = {"Mom": "July 2nd",
             "Dad": "October 25th",
             "Wife": "January 21st",
             "Brother": "June 27th",
             "Sister": "February 24th"}

while True:
    # User input.
    print("Enter a name: (blank to quit)")
    name = input().strip().capitalize()

    # Quit program if input is blank.
    if name == "":
        break

    # If name is found, print birthday.
    if name in birthdays:
        print("{}'s birthday is on {}.\n".format(name, birthdays[name]))

    # If name is not found, update database.
    else:
        print("I do not have birthday information for {}.".format(name))
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.\n")
