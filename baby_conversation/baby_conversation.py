# Baby conversation simulator program to test the "while" loop.

# Import choice from the random module.
from random import choice

# Create list of questions.
questions = ["Why is the sky blue?",
             "When did the world begin?",
             "How do you do that?",
             "Why are you so strong?",
             "Is there a face on Mars?"]

# Print question.
print(choice(questions))

# Require an answer.
answer = input().strip()

while answer != "Just because.":
    # Baby's question.
    print("But why?")
    # Require more explanation. :)
    answer = input().strip()

# Baby stops asking questions.
print("Oh, Okay.")
