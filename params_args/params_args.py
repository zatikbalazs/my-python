# Learn about parameters, default parameters,
# arguments and keyword arguments.

# PARAMETERS of the function.
def add(a, b):
    return a + b

# Pass ARGUMENTS to the function.
add(1, 2)


# Default parameters.
# WARNING! Default params must always go after "normal" params!
def about(name, age, hobby = "Python"):
    sentence = "Name: {}. Age: {}. Hobby: {}.".format(name, age, hobby)
    return sentence

about("Tom", 30)

# Keyword arguments.
about(age = 40, name = "Jennifer")
