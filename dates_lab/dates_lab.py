"""
Dates Lab - Coding Exercise
"""

# Import modules.
import time
import datetime

# Today's date.
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

# ISO format.
my_birthday = datetime.datetime(1985, 10, 2, 12, 00, 00)
print("I was born on:", my_birthday.isoformat(" "))
