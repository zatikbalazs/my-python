# Tuple & Dictionary Lab Exercise
# -------------------------------
# Step 1: Using a for loop, loop through each element of the gpas
#         tuple and output the average gpa stored in the tuple.
#
# Step 2: Instead of using a tuple, let's store the same data in
#         a dictionary so that each GPA value is identified by a
#         string key containing the name of the person who achieved
#         the GPA.
#
# Step 3: Using the dictionary you just created, again calculate
#         the average and output the average, and who achieved the
#         highest and lowest GPA from the dictionary.

# ------
# Step 1
# ------

# Create tuple.
gpas = (2.25, 3.45, 3.81, 2.99, 3.76)

# Create variable to store total value.
total = 0

# Loop through the tuple.
for gpa in gpas:
    total += gpa

# Calculate average.
average = total / len(gpas)

# Output rounded average.
print("Average GPA is:", round(average, 2))


# ------
# Step 2
# ------

# Create dictionary.
gpas = {"Bob": 3.45,
        "Alice": 3.84,
        "John": 2.88,
        "Jennifer": 3.55,
        "Michael": 3.67}


# ------
# Step 3
# ------

# Initialize variables.
total = 0
highest_gpa  = 0
highest_name = None
lowest_gpa   = 4.0
lowest_name  = None


# Loop through all items in the dictionary.
for key, value in gpas.items():

    # Increment total value.
    total += value

    # Set highest GPA and name.
    if value >= highest_gpa:
        highest_gpa  = value
        highest_name = key

    # Set lowest GPA and name.
    if value <= lowest_gpa:
        lowest_gpa  = value
        lowest_name = key


# Calculate average.
average = total / len(gpas)

# Output rounded average.
print("Average GPA is:", round(average, 2))

# Who achieved the highest GPA?
print("Highest GPA: {} ({})".format(highest_gpa, highest_name))

# Who achieved the lowest GPA?
print("Lowest GPA:  {} ({})".format(lowest_gpa, lowest_name))
