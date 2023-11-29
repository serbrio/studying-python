#!/usr/bin/env python3

from leap_years import is_year_leap


def days_in_month(year, month):
    if month not in range(1, 13) or year < 1582:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return days[month - 1]


test_years = [1900, 2000, 2016, 1987, 1999, 1581]
test_months = [2, 2, 1, 11, 15, 3]
test_results = [28, 29, 31, 30, None, None]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
