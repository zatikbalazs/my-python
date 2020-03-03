# Read content of a text file.
# Step 1: open file with open().
# Step 2: read content with read().

# Open file.
try:
    file_path = "example.txt"
    file = open(file_path)

    # Read and print the file's content to console.
    print(file.read())

except FileNotFoundError:
    print("File not found! [{}]".format(file_path))
