# Generating random values in Python.

# Import random module.
import random

# Random float: 0.0 <= n < 1.0
result = random.random()
print(result)

# Random float:  2.5 <= n < 10.0
result = random.uniform(2.5, 10.0)
print(result)

# Random integer between two values (both are inclusive).
result = random.randint(1, 100)
print(result)

# Random integer from 0 to 9 inclusive.
result = random.randrange(10)
print(result)

# Random range. Start (inclusive), stop (exclusive), step.
result = random.randrange(0, 101, 10)
print(result)

# Random choice from iterables.
fruits = ["apple", "banana", "peach", "watermelon", "strawberry"]
result = random.choice(fruits)
print(result)

string = "Beautiful"
result = random.choice(string)
print(result)

# Shuffle a list.
random.shuffle(fruits)
print(fruits)

# Get a random sample from a list.
animals = ["dog", "cat", "horse", "mouse", "chicken"]
result = random.sample(animals, k=3)
print(result)
