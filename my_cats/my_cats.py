# Create list to store cats.
cats = []

while True:
    # Collect data from user.
    print("Enter the name of cat " + str(len(cats) + 1) + " (Or enter nothing to stop.)")
    name = input().strip()

    # If user enters nothing, the loop breaks.
    if name == "":
        break

    # If user enters a name, the name gets appended to the list.
    else:
        cats.append(name)

# When the loop is over, we print the list of cats.
print("These are my cats:")
for cat in cats:
    print(cat)
