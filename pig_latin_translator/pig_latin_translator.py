# Import module (Regular Expression).
import re

# Get sentence from user.
original = input("Please enter a sentence: ").strip().lower()

# Split up sentence into words.
words = original.split()

# Create list for new words.
new_words = []

# Loop through words and convert to pig latin.
for word in words:

    # If the word starts with a vowel,
    # we simply add "yay" to the end.
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)

    # If the word starts with a consonant,
    # we slice the word at the first vowel.
    else:
        vowel_position = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_position += 1
            else:
                break

        # Slice and create new word.
        beginning = word[:vowel_position]
        the_rest = word[vowel_position:]
        new_word = the_rest + beginning + "ay"

        # Add new word to list.
        new_words.append(new_word)

# Stick the new words together.
new_sentence = " ".join(new_words)

# Remove punctuation from new sentence.
new_sentence = re.sub("[\.\?\!\,]", "", new_sentence)

# Capitalize first word and add period to the end.
output = new_sentence.capitalize() + "."

# Print output.
print(output)
