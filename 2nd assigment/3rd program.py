'''Write a Python program to display calendar?'''

import calendar
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

if year == 0:
    print("invalid year")
elif month<=0 and month>12:
    print(calendar.month(year, month))
else:
    print("invalid month")
    





