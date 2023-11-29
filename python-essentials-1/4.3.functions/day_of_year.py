#!/usr/bin/env python3

from leap_years import is_year_leap
from how_many_days import days_in_month


def day_of_year(year, month, day):
    # use days_in_month() to check if year and month are valid
    if days_in_month(year, month) == None:
        return None
    
    days = 0
    for m in range(1, month):
        days += days_in_month(year, m)
    
    if day >= 1 and day <= days_in_month(year, month):
        days += day
        return days
    else:
        return None


def test():
    assert day_of_year(1999, 1, 1) == 1
    assert day_of_year(2023, 2, 1) == 32
    assert day_of_year(2023, 11, 29) == 333
    assert day_of_year(1956, 2, 30) == None

test()
