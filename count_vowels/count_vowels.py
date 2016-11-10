# Initialize variables.
vowels = 0
consonants = 0

# User input.
word = input("Please enter a word: ").strip().lower()

# Iterate over characters of word.
for char in word:
    if char in "aeiou":
        vowels += 1
    elif char == " ":
        pass
    else:
        consonants += 1

# Print results.
print("vowels: {}, consonants: {}".format(vowels, consonants))
