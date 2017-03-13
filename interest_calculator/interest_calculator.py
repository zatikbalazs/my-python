# Simple Interest Calculator Program

# Define functions.
def header(title):
    """
    Prints out a nice header.
    params: str(title)
    return: str(header)
    """
    # Get the length of title.
    length = len(title)

    # Concatenate header string.
    header = "=" * length + "\n" + title.upper() + "\n" + "=" * length

    return header


# Print header.
print(header("Simple Interest Calculator"))

# User input.
balance = float(input("Starting balance ($): ").strip())
interest_rate = float(input("Yearly interest(%): ").strip())
term = int(input("How many months? ").strip())

# Print starting conditions.
print()
print("Starting balance: $%.2f | Yearly interest: %.2f percent | Term: %d months" % (balance, interest_rate, term))
print()

# Calculate and show monthly results.
for month_num in range(1, term + 1):
    interest = balance * (interest_rate / 100 / 12)
    balance += interest
    print("Month #%d \t Monthly interest: $%.2f \t Balance: $%.2f" % (month_num, interest, balance))
