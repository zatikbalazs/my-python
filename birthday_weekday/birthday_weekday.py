# What weekday were you born on?

# Import module.
import calendar

# Define functions.
def header(title):
    # Prints out a nice header.
    # params: str(title)
    # return: str(header)

    # Get the length of title.
    length = len(title)

    # Concatenate header string.
    header = "=" * length + "\n" + title.upper() + "\n" + "=" * length

    return header


# Print header.
print(header("What weekday were you born on?"))

# User input.
print("Your date of birth:")

while True:
    try:
        year = int(input("Year: ").strip())
        break
    except ValueError:
        print("Only numbers please!")
        continue

while True:
    try:
        month = int(input("Month: ").strip())
        break
    except ValueError:
        print("Only numbers please!")
        continue

while True:
    try:
        day = int(input("Day: ").strip())
        break
    except ValueError:
        print("Only numbers please!")
        continue

# Get the weekday.
day_num = calendar.weekday(year, month, day)

# Add a string representation.
if day_num == 0:
    day_str = "Monday"
elif day_num == 1:
    day_str = "Tuesday"
elif day_num == 2:
    day_str = "Wednesday"
elif day_num == 3:
    day_str = "Thursday"
elif day_num == 4:
    day_str = "Friday"
elif day_num == 5:
    day_str = "Saturday"
elif day_num == 6:
    day_str = "Sunday"

# Print result.
print("You were born on:", day_str)
