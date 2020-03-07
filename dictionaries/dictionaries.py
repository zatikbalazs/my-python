# The basics of using dictionaries in Python.

# Create a dictionary.
player = {"name": "Doodle",
          "age": 30,
          "exp": 1500,
          "rank": "Rookie"}

# Print a dictionary.
print(player)

# Access a value.
name = player["name"]
print(name)

# Alternative method to get a value.
age = player.get("age")
print(age)

# Change a value.
player["age"] = 31
print(player["age"])

# Delete a key-value pair.
del player["rank"]
print(player)

# Length. (The number of key-value pairs.)
print(len(player))

# Stringify a dictionary.
print(str(player))

# Remove all keys and values from the dictionary.
# player.clear()
# print(player)

# Get all items.
print(player.items())

# Get all the keys.
print(player.keys())

# Check whether a key exists or not (1).
if "name" in player.keys():
    print(True)
else:
    print(False)

# Check whether a key exists or not (2).
if "name" in player:
    print(True)
else:
    print(False)

# Get all the values.
print(player.values())

# Loop through all of the keys.
for p in player:
    print(p)

# Loop through all of the keys and values.
for key, value in player.items():
    print(key, value)
