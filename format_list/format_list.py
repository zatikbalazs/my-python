# Define function.
def format_list(mylist):
    """
    This function transforms a list into a formatted string.
    args: list(mylist)
    return: str(string)
    """

    # Initialize variable.
    string = ""

    # Get the length of the list.
    list_length = len(mylist)

    # Concatenate strings.
    for index, item in enumerate(mylist):

        # Separate items with commas.
        if index < list_length - 2:
            string += item + ", "

        # Use "and" before the last item.
        elif index == list_length - 2:
            string += item + ", and "

        # The last item.
        else:
            string += item

    # Return value of function.
    return string

# Create list.
fruits = ["apple", "banana", "orange", "kiwi", "strawberry", "watermelon"]

# Call function and print return value.
print(format_list(fruits))
