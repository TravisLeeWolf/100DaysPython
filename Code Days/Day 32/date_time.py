import datetime as dt

now = dt.datetime.now()
year = now.year
dayOfWeek = now.weekday()
print(dayOfWeek)

# You can also create your own datetime object
dateOfBirth = dt.datetime(year=1969, month=4, day=20)
print(dateOfBirth)