# Create movies database (dictionary).
movies = {
    "Terminator":   {"age": 16, "seats": 1},
    "Gladiator":    {"age": 12, "seats": 2},
    "Yes Man":      {"age": 6,  "seats": 3},
    "Pulp Fiction": {"age": 12, "seats": 4},
    "Minions":      {"age": 3,  "seats": 5}
    }

# Welcome visitor.
print("Welcome to the Python Box Office! :)".upper())

# Show available movies.
print("The following movies are playing right now:\n")
for key, value in movies.items():
    movie_title = key
    seats_left = value["seats"]
    print("{0} - available seats: {1}".format(movie_title, seats_left))

while True:
    # Visitor enters title of movie.
    choice = input("\nWhat movie would you like to watch? ").strip().title()

    # If the movie is found.
    if choice in movies:

        try:
            # Age of visitor.
            age = int(input("How old are you? ").strip())

            # Age can only be a positive integer.
            if age > 0:

                # Check visitor's age.
                if age >= movies[choice]["age"]:

                    # Check seats available.
                    if movies[choice]["seats"] > 0:

                        # Decrease the number of seats available.
                        movies[choice]["seats"] = movies[choice]["seats"] - 1

                        print("Here is your ticket. Enjoy the movie!")
                        print("Number of remaining free seats for this movie: {}".format(movies[choice]["seats"]))

                        # Buy another ticket?
                        another = input("\nWould you like to buy another ticket? (y/n) ").strip().lower()

                        if another == "y" or another == "yes":
                            continue
                        else:
                            print("Thank you.")
                            break

                    else:
                        print("Sorry, there are no more seats available.")

                else:
                    print("You are too young to see this movie!")

            else:
                print("Invalid input for age.")
        except ValueError:
            print("Invalid input for age.")

    # If the movie is not found.
    else:
        print("Sorry, we don't have that movie.")
