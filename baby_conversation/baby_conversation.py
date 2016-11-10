# Baby conversation simulator program to test "while" loop.

# Import module.
import random

# Create list of questions.
questions = ["Why is the sky blue?",
             "When did the world begin?",
             "How do you do that?",
             "Why are you so strong?",
             "Is there a face on Mars?"]

# Print question.
print(random.choice(questions))

# Require an answer.
answer = input().strip()

while answer != "Just because.":
    # Baby's question.
    print("But why?")
    # Require more explanation. :)
    answer = input().strip()

# Baby stops asking questions.
print("Oh, Okay.")
