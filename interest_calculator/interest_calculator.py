# Simple Interest Calculator Program

# Define functions.
def header(title):
    # Print out a nice header.
    # params: str(title)
    # return: str(header)

    # Get the length of title.
    length = len(title)

    # Concatenate header string.
    header = "=" * length + "\n" + title.upper() + "\n" + "=" * length

    return header


# Print header.
print(header("Simple Interest Calculator"))

# User input.
while True:
    try:
        balance = float(input("Starting balance ($): ").strip())
        break
    except ValueError:
        print("Only numbers are accepted! Correct format: 1000.00")
        continue

while True:
    try:
        interest_rate = float(input("Yearly interest (%): ").strip())
        break
    except ValueError:
        print("Only numbers are accepted! Example: 2.25")
        continue

while True:
    try:
        term = int(input("How many months? ").strip())
        break
    except ValueError:
        print("Only numbers are accepted! Example: 120")
        continue

# Print starting conditions.
print()
print("Starting balance: $%.2f | Yearly interest (percent): %.2f | Term: %d months" % (balance, interest_rate, term))
print()

# Calculate and show monthly results.
for month_num in range(1, term + 1):
    interest = balance * (interest_rate / 100 / 12)
    balance += interest
    print("Month #%d \t Monthly interest: $%.2f \t Balance: $%.2f" % (month_num, interest, balance))
