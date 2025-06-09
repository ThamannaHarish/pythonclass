#Part 1: Using calendar module

import calendar
from datetime import datetime,timedelta

month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

print("\nPart 1: Calendar using calendar module\n")
cal = calendar.month(year, month)
print(cal)

#Part 2: Using datetime module (without calendar module)

print("Part 2: Calendar using datetime module\n")

first_day = datetime(year, month, 1)
current_day = first_day
while current_day.month == month:
    print(current_day.strftime("%A, %d %B %Y"))
    current_day += timedelta(days=1)
    
