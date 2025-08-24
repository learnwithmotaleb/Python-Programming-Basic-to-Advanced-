# from datetime import date, datetime


# now = datetime.now()
# print(now)


# # Specific date
# d = date(2025, 8, 25)
# print("Date:", d)


# print(now.strftime("%d-%m-%Y %H:%M:%S"))
# now = datetime.now()
# print("Now:", now)                # Full date & time
# print("Year:", now.year)          # Year
# print("Month:", now.month)        # Month
# print("Day:", now.day)            # Day
# print("Hour:", now.hour)          # Hour
# print("Minute:", now.minute)      # Minute
# print("Second:", now.second)      # Second
# print("Microsecond:", now.microsecond)


# now = datetime.now()

# print(now.strftime("%d-%m-%Y"))      # 25-08-2025
# print(now.strftime("%B %d, %Y"))     # August 25, 2025
# print(now.strftime("%I:%M %p"))      # 12-hour format: 04:30 PM
# print(now.strftime("%H:%M:%S"))      # 24-hour format: 16:30:45


# # 

from datetime import datetime, timedelta

# Time difference
delta = timedelta(days=5, hours=3)
print("Delta:", delta)

# Add delta to current time
future = datetime.now() + delta
print("Future Date:", future)
