# Import module (Regular Expression).
import re

# Define functions.
def header(title):
    """
    Prints out a nice header.
    args: str(title)
    return: str(header)
    """
    # Get the length of title.
    length = len(title)

    # Concatenate header string.
    header = "=" * length + "\n" + title.upper() + "\n" + "=" * length

    return header

def get_line_count(filename):
    """
    Counts number of lines in a file.
    args: str(filename)
    return: int(line_count)
    """
    with open(filename) as file:
        line_count = sum(1 for _ in file)

    return line_count

def get_char_list(text, sort=True):
    """
    Creates statistics for all characters in text.
    args: str(text), bool(sort)
    return list(char_list)
    """
    char_dict = {}

    for char in text.lower():
        char_dict.setdefault(char, 0)
        char_dict[char] = char_dict[char] + 1

    # Sort dictionary by values. (Creates a list.)
    char_list = sorted(char_dict.items(), key=lambda x:x[1], reverse=sort)

    return char_list

def get_word_list(text, sort=True):
    """
    Creates statistics for all words in text.
    args: str(text), bool(sort)
    return list(word_list)
    """
    word_dict = {}

    text_clean = re.sub("[\.\?\!]", "", text).lower()

    for word in text_clean.split():
        word_dict.setdefault(word, 0)
        word_dict[word] = word_dict[word] + 1

    # Sort dictionary by values. (Creates a list.)
    word_list = sorted(word_dict.items(), key=lambda x:x[1], reverse=sort)

    return word_list

def get_keyword_density(keyword, text):
    """
    Calculate keyword density in the given text.
    args: str(keyword), str(text)
    return int(keyword_count), float(keyword_density)
    """
    # Prepare keyword and text.
    keyword = keyword.lower()
    text_clean = re.sub("[\.\?\!]", "", text).lower()

    # Get word count.
    word_count = len(text.split())

    # Get keyword count.
    keyword_count = text.count(keyword)

    # Get keyword density.
    keyword_density = (keyword_count / word_count) * 100
    keyword_density = round(keyword_density, 2)

    return keyword_count, keyword_density


# Execute functions.

# Print header.
print(header("Text Statistics"))

try:
    # User input.
    filename = input("Enter the name of the text file (hint: sample.txt): ").strip()
    keyword = input("Enter your keyword: ").strip()

    # User must enter a keyword.
    while keyword == "":
        keyword = input("Enter your keyword: ").strip()

    # Open file.
    file = open(filename)

    # Read in text from file.
    text = file.read().strip()

    # Character count and word count.
    char_count = len(text)
    word_count = len(text.split())

    # How many lines are there in the file?
    line_count = get_line_count(filename)

    # Get statistics for all characters in text.
    char_list = get_char_list(text)

    # Get statistics for all words in text.
    word_list = get_word_list(text)

    # Get keyword density.
    keyword_count, keyword_density = get_keyword_density(keyword, text)


    # Print results.
    print("\nMost common characters:")
    for item in char_list:
        print(item)

    print("\nMost common words:")
    for item in word_list:
        print(item)

    print("\n{} lines, {} words, {} characters.".format(line_count, word_count, char_count))

    print("\nYour keyword is: \"{}\"".format(keyword))
    print("Keyword count: {}, keyword density: {}%".format(keyword_count, keyword_density))

except FileNotFoundError:
    print("Error: File not found!")
