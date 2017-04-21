"""
The basics of dictionaries in Python.
"""

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

# Change a value.
player["age"] = 31
print(player["age"])

# Delete a key-value pair.
del player["rank"]
print(player)
