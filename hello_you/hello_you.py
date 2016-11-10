# Intro message.
print("Hello, I want to get to know you better.")

# Collect data from user.
name = input("What is your name? ")
age = input("How old are you? ")
place = input("Where are you from? ")

# Prepare output string.
string = """Your name is {} and you are {} years old.
I'm sure {} is a beautiful place!"""
output = string.format(name, age, place)

# Print output.
print(output)
