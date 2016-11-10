# Import modules.
import random

# Create list of quotes.
quotes = ["\"With gratitude for everything, success and victory will be yours.\" - Sadhguru",
          "\"No job is inherently stressful. What causes stress is our compulsive reaction to challenging situations.\" - Sadhguru",
          "\"Every cell in your body is working for your wellbeing. If you are in tune with your system, you will naturally be healthy.\" - Sadhguru",
          "\"With absolute involvement, any activity can become a spiritual process.\" - Sadhguru",
          "\"The life within you cannot be unpleasant. Unpleasantness is created in the mind.\" - Sadhguru",
          "\"Mastery of anything does not come without absolute devotion.\" - Sadhguru",
          "\"Success is not in doing more. It’s in doing the right things.\" - Sadhguru",
          "\"Once you go beyond the mind, there is no such thing as suffering.\" - Sadhguru",
          "\"Meditation is a means to realize the beauty of your existence.\" - Sadhguru",
          "\"Until you have become boundless, you cannot call yourself successful.\" - Sadhguru",
          "\"You want to be loved because you feel incomplete. Otherwise, being loved can be quite a nuisance.\" - Sadhguru",
          "\"If you become full-blown consciousness, everything that can be known will be known to you.\" - Sadhguru"]

# Welcome user.
print("=" * 25)
print("Welcome to random quotes!".upper())
print("=" * 25)
print("Today's quote is:")

# Initialize quote indexes.
prev_index = None
next_index = None

while True:
    # Next index cannot be equal to previous index.
    while next_index == prev_index:
        next_index = random.randint(0, len(quotes) - 1)

    # Show random quote.
    print(quotes[next_index])

    # Ask user if he/she wants to see another quote.
    another = input("\nWould you like to see another quote? (y/n) " ).strip().lower()

    if another == "y" or another == "yes":
        prev_index = next_index
        continue
    elif another == "n" or another == "no":
        print("See you tomorrow!")
        break
    else:
        print("Invalid input. Program terminated.")
        break
