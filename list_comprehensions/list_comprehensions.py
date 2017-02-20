# Practice list comprehensions.

# Simple example.
even_numbers = [number for number in range(1,21) if number % 2 == 0]

print(even_numbers)

# Create a list of lists based on another list.
countries = ["Hungary", "Germany", "France", "USA", "Russia"]
result = [[country.upper(), len(country)] for country in countries]

print(result)
