#Write a Python function that checks whether a given year is a leap year.


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = 2020
print(f"{year} is a leap year: {is_leap_year(year)}")


year = 1900
print(f"{year} is a leap year: {is_leap_year(year)}")