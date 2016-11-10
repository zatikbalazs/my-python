# Collect data from user.
print("Please enter your email address:")
email = input("Email: ").strip()

# Check if email is empty.
if len(email) > 0:
    # Check if email is valid.
    if email.count("@") == 1:
        # Slice email address.
        user = email[:email.index("@")]
        domain = email[email.index("@") + 1:]

        # Print result.
        print("Username: {}".format(user))
        print("Domain: {}".format(domain))
    else:
        print("Not a valid email address!")
else:
    print("You didn't enter anything.")
