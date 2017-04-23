"""
Handling time in Python.
"""

# Import module.
import time

# Number of seconds from unix epoch.
output = time.time()
print(output)

# Local time (time tuple).
output = time.localtime(time.time())
print(output)

# Formatted local time.
output = time.asctime(time.localtime(time.time()))
print(output)
