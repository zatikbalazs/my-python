# Create list.
names = []

# Make user enter "n" number of names.
while len(names) < 5:
    name = input("Please add a name: ").strip().title()
    # Append name to list.
    names.append(name)

# If list is full.
print("\nSorry, the list is full:")
print("=" * 24)

for name in names:
    print(name)
