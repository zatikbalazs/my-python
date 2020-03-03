# Define functions.
def print_inventory(inventory):
    # Prints inventory with values.
    # params: dict(inventory)

    total_items = 0

    print("Inventory:".upper())

    # Iterate through the keys and values of dictionary.
    for key, value in inventory.items():

        # Print every key with its correspoding value.
        print("{}: {}".format(key, value))

        # Update total value.
        total_items += value

    print("\nTotal number of items: {}".format(total_items))


def add_to_inventory(inventory, new_items):
    # Adds new items to an existing inventory.
    # params: dict(inventory), list(new_items)
    # return: dict(inventory)

    # Iterate through items of the list.
    for item in new_items:

        # If item does not exist in the inventory yet,
        # then create the key and set the default value to 0!
        # Why 0? Because we will update the key's value below.
        inventory.setdefault(item, 0)

        # If item already exists in the inventory,
        # then update its value.
        inventory[item] += 1

    return inventory


# Create an inventory.
inventory = {"chair": 10, "computer": 8, "printer": 3, "plant": 12, "table": 8}

# Create a list of new items.
new_items = ["computer", "computer", "computer", "table", "table", "table", "car"]


# Call functions.

# Print original inventory.
print_inventory(inventory)

# Show items to be added.
print("\nItems to be added:")
for new_item in new_items:
    print(new_item)
print()

# Add new items to inventory.
new_inventory = add_to_inventory(inventory, new_items)

# Print the new inventory.
print_inventory(new_inventory)
