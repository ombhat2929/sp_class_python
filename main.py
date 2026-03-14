import datetime

# Get today's date
today = datetime.date.today()

# Day of the week (Monday=0, Sunday=6)
day_number = today.weekday()

# Day name (like Monday, Tuesday, etc.)
day_name = today.strftime("%A")

print("Today's date:", today)
print("Day number:", day_number)
print("Day name:", day_name)