#!/usr/bin/env python3

from leap_years import is_year_leap


def days_in_month(year, month):
    thirty_days_month = [4, 6, 9, 11]
    if month not in range(1, 13):
        return None

    if month in thirty_days_month:
        return 30
    elif month != 2:
        return 31
    elif is_year_leap(year):
        return 29
    else:
        return 28



test_years = [1900, 2000, 2016, 1987, 1999]
test_months = [2, 2, 1, 11, 15]
test_results = [28, 29, 31, 30, None]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
