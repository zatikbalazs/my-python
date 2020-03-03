# This is my collection of the most useful string methods.

# This example string will be used throughout the file.
string = "Silence will breed wisdom."


# Length.
result = len(string)
print(result) # 26

# Count.
result = string.count("e")
print(result) # 4

# Count (in a part of the string).
result = string.count("e", 0, 7)
print(result) # 2

# Slice (one character).
result = string[4]
print(result) # n

# Slice (multiple characters).
result = string[:4]
print(result) # Sile

# Index.
result = string.index("i")
print(result) # 1

# Find.
result = string.find("x")
print(result) # -1

# Uppercase.
result = string.upper()
print(result) # SILENCE WILL BREED WISDOM.

# Is uppercase?
result = string.isupper()
print(result) # False

# Lowercase.
result = string.lower()
print(result) # silence will breed wisdom.

# Is lowercase?
result = string.islower()
print(result) # False

# Swapcase.
result = string.swapcase()
print(result) # sILENCE WILL BREED WISDOM.

# Capitalize.
result = string.capitalize()
print(result) # Silence will breed wisdom.

# Title.
result = string.title()
print(result) # Silence Will Breed Wisdom.

# Is title?
result = string.istitle()
print(result) # False

# Is alpha?
result = string.isalpha()
print(result) # False

# Is alphanumeric?
result = string.isalnum()
print(result) # False

# Is digit?
result = string.isdigit()
print(result) # False

# Is decimal?
result = string.isdecimal()
print(result) # False

# Strip.
result = string.strip()
print(result) # Silence will breed wisdom.

# Left strip.
result = string.lstrip("S")
print(result) # ilence will breed wisdom.

# Strip.
result = string.rstrip(".")
print(result) # Silence will breed wisdom

# Center.
result = string.center(50, "*")
print(result) # ************Silence will breed wisdom.************

# Join.
fruits = ["apple", "orange", "kiwi", "cherry"]
result = " | ".join(fruits)
print(result) # apple | orange | kiwi | cherry

# Split (default).
result = string.split()
print(result) # ['Silence', 'will', 'breed', 'wisdom.']

# Split (custom).
result = string.split(" ")
print(result) # ['Silence', 'will', 'breed', 'wisdom.']

# Starts with?
result = string.startswith("A")
print(result) # False

# Ends with?
result = string.endswith(".")
print(result) # True

# Format.
result = "I have {} sisters.".format(2)
print(result) # I have 2 sisters.

# Is space?
result = "  ".isspace()
print(result) # True

# Replace.
result = string.replace("wisdom", "knowledge")
print(result) # Silence will breed knowledge.

# Split lines.
multi_lines = "First line\n"
multi_lines += "Second line\n"
multi_lines += "Third line"
result = multi_lines.splitlines()
print(result) # ['First line', 'Second line', 'Third line']

# Zfill.
result = string.zfill(40)
print(result) # 00000000000000Silence will breed wisdom.
