# Demonstration of different cases
# regarding the scopes of variables.

# CASE 1:
# Global and local variables are completely separated.

# Global variable.
a = 1

def func1():
    a = 2 # Local variable.
    print(a)

def func2():
    a = 3 # Local variable.
    print(a)


func1()
func2()

# Print the value of the global variable.
print(a)


print()


# CASE 2:
# Read the value of a global variable in a local scope.

# Global variable.
a = 1

def func1():
    # Read in global variable.
    b = a + 10
    print(b)

def func2():
    a = 3 # Local variable.
    print(a)


func1()
func2()

# Print the value of the global variable.
print(a)


print()


# CASE 3:
# Overwrite the value of a global variable in a local scope.

# Global variable.
a = 1

def func1():
    # Overwrite global variable.
    global a
    a = 10
    print(a)

def func2():
    a = 3 # Local variable.
    print(a)


func1()
func2()

# Print the value of the global variable.
print(a)


print()


# CASE 4:
# The special case of lists and dictionaries.
# You cannot overwrite the whole list or dictionary
# but you can overwrite a little part of them.

# Global variables.
a = [1, 2, 3, 4, 5]
b = {"Tom": 34, "Jane": 22, "Erica": 18}

def func1():
    # Overwrite a little part.
    a[0] = 10
    b["Jane"] = 12

    # Values of overwritten global variables will be printed.
    print(a)
    print(b)

def func2():
    # Values of overwritten global variables will be printed.
    print(a)
    print(b)


func1()
func2()

# Print the values of the global variables.
print(a)
print(b)
