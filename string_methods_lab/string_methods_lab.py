# String Methods Lab
# ------------------
# Step 1: Create some multi-line text and store it in a variable.
# Step 2: Using a loop, output each line and character number of the string.
#         For example line 2, character 2 is an "a".
# Step 3: Alter your code so that the word "Capital" is printed to the right
#         of each capital letter in your output.
# Step 4: Indicate new lines in your output with the text: "- New Line -"

# Create multi-line text.
text  = "This is the first line of my text.\n"
text += "The text continues with the second line.\n"
text += "We have come to the last line."

# Initialize variables.
char = 0
line = 1

# Loop through each character of the text.
while char < len(text):

    # Get current character.
    current_char = text[char]

    # If it is not a new line.
    if current_char != "\n":
        if current_char.isupper():
            print("Line:{} Char:{}\t{} Capital".format(line, char, current_char))
        else:
            print("Line:{} Char:{}\t{}".format(line, char, current_char))

    # If it is a new line.
    else:
        print("Line:{} Char:{}\t- New Line -".format(line, char))
        line += 1

    # Increment value to get to next character in the loop.
    char += 1
