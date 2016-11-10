# Open file and read in password.
file = open("secretpassword.txt")
password = file.read().strip()

# Get password from user.
print("What is your password?")
typed_password = input()

# Check if password is correct.
if typed_password == password:
    print("Access granted.")
else:
    print("Access denied.")
