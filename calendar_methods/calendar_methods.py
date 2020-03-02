# Calendar methods in Python.

# Import module.
import calendar

# Show calendar.
cal = calendar.month(1985, 10)
print(cal)

# Get first weekday of the calendar.
output = calendar.firstweekday()
print(output)

# Set first weekday of the calendar.
output = calendar.setfirstweekday(calendar.SUNDAY)

# Get day of the week.
output = calendar.weekday(1985, 10, 2)
print(output)

# Is leap year?
output = calendar.isleap(2020)
print(output)
