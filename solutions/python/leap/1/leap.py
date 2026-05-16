"""This module determines whether a given year is a leap year.

A leap year (in the Gregorian calendar) occurs:

- In every year that is evenly divisible by 4.
- Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.
"""


def leap_year(year):
    """Determines whether a given year is a leap year.

    Args:
        year: The year to check, as an integer.

    Returns:
        True if the year is a leap year, False otherwise.
    """
    
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
