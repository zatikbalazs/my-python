def reverse_string(string):
    """
    Reverse any string.
    args: str(string)
    return: str(reversed_string)

    Note: this function can reverse any
    iterable data type (string, list, tuple).
    """
    # Reverse the string.
    reversed_string = string[::-1]

    return reversed_string


# User enters string.
string = input("Enter the text you want to reverse: ").strip()

# Call the function.
reversed_string = reverse_string(string)

# Print reversed string.
print(reversed_string)
