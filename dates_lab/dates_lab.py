"""
Dates Lab - Coding Exercise
"""

# Import module.
import time

# Current date.
today = time.asctime(time.localtime(time.time()))

# Tomorrow's date.
tomorrow = time.asctime(time.localtime(time.time()+60*60*24))

# A year ago.
year_ago = time.asctime(time.localtime(time.time()-60*60*24*365))

# In 100 hours.
hundred_hours = time.asctime(time.localtime(time.time()+60*60*100))

# Print output.
print("Today it is:", today)
print("Tomorrow it will be:", tomorrow)
print("A year ago it was:", year_ago)
print("In 100 hours it will be:", hundred_hours)
