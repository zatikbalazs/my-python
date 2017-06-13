# Rounding numbers in Python.

# Import math module.
import math

# Our example number.
number = math.pi # 3.141592653589793

# ---------------------------------
# Using the inbuilt round() method.
# Be aware that this method uses
# the so called banker's rounding!
# ---------------------------------
"""
What is banker's rounding?
--------------------------
.5 will be rounded to the nearest
EVEN integer, or 0. Examples:
0.5 => 0
1.5 => 2
2.5 => 2
3.5 => 4
"""

# Round to nearest integer.
result = round(number)
print(result)

# Round to n digits.
result = round(number, 2)
print(result)

# -----------
# Formatting.
# -----------

# Round down to nearest integer.
print("%d" % (number))

# Round to n digits.
print("%.2f" % (number))
print("%.4f" % (number))

# ----------------------
# Using the math module.
# ----------------------

# Round up to nearest integer.
result = math.ceil(number)
print(result)

# Round down to nearest integer.
result = math.floor(number)
print(result)

# --------
# Casting.
# --------

# Round down to nearest integer.
result = int(number)
print(result)
