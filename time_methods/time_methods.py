# The most common time methods in Python.

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

# GMT.
output = time.gmtime(time.time())
print(output)

# Sleep for "n" seconds.
time.sleep(1)

# Time of current process.
output = time.process_time()
print(output)

# Format time.
output = time.strftime("%Y.%m.%d. %H:%M:%S")
print(output)

# Parse time.
output = time.strptime("30 Nov 00", "%d %b %y")
print(output)
