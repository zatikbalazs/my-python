# Write to a text file.
#
# Step 1: open file with open().
# Step 2: write to file with write().
# Step 3: close file with close().

# Open file for writing.
file = open("example.txt", "w") # Use "a" to append to the end of file.

# Create an empty list of names.
names = []

# User has to enter 3 names.
while len(names) <= 2:
    name = input("Enter a name: ").strip().title()
    names.append(name)

print("Saving names... {}".format(names))

# Write to file (as a string).
try:
    file.write(str(names))

    # Close file.
    file.close()

    print("Names saved!")

except IOError:
    # Close file.
    file.close()

    print("IO Error!")
