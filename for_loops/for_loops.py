# Using for loops to iterate through different data types.

# String.
name = "John Smith"

for char in name:
    print(char)


print()


# Simple list.
my_animals = ["dog", "cat", "chicken"]

for my_animal in my_animals:
    print(my_animal)


print()


# List within a list.
animals = ["horse", "mouse", "elephant", my_animals]

for animal in animals:
    print(animal)


print()


# Lists within a list.
countries = [["USA", "Canada", "Mexico"],
             ["Germany", "France", "Great Britain"],
             ["Hungary", "Poland", "Croatia"]]

for i in range(3):
    for country in countries[i]:
        print(country)


print()


# Tuple.
numbers = (1, 2, 3, 4, 5)

for number in numbers:
    print(number)


print()


# Simple dictionary.
movies = {"The Godfather": 92, "Forrest Gump": 88, "Gladiator": 82}

for movie in movies:
    print(movie)

print()

for key, value in movies.items():
    print(key, value)


print()


# Lists within a dictionary.
students = {"males": ["John", "George", "Tom"],
            "females": ["Erica", "Jennifer", "Kate"]}

for student in students:
    print(student)

print()

for key, value in students.items():
    print(key, value)

print()

for key in students.keys():
    for name in students[key]:
        print(name)


print()


# Dictionaries within a dictionary.
employees = {"John Smith": {"age": 32, "salary": 108000, "position": "developer"},
             "Kevin Boyle": {"age": 62, "salary": 158000, "position": "team leader"},
             "Erica Longdon": {"age": 28, "salary": 90000, "position": "designer"}}

for employee in employees:
    print(employee)

print()

for key, value in employees.items():
    print(key, value)

print()

for key, value in employees.items():
    print(key, value["age"])

print()

for key, value in employees.items():
    print(key.upper())
    for key2, value2 in value.items():
        print("{}: {}".format(key2, value2))
    print()
