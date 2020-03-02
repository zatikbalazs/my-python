def fibonacci(n):
    # Fibonacci sequence up to "n".

    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b

# Intro text.
print("Generate the Fibonacci sequence.")

try:
    # Get max. number from user.
    max_number = int(input("Please enter the max. number: ").strip())

    # Only accept positive integer numbers.
    if max_number > 0:
        # Call the fibonacci() function with "max_number".
        fibonacci(max_number)
    else:
        print("Only positive integer numbers are accepted.")

except ValueError:
    print("Sorry, only numbers are accepted.")
