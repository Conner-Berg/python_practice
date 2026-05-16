"""This module determines whether a number is an Armstrong number.

An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
"""


def is_armstrong_number(number):
    """Determine if a given number is an Armstrong number.

    Args:
        number (int): Any whole number.

    Returns:
        bool: If the numbers fits the Armstrong number criteria.
    """

    num_digits = len(str(abs(number)))
    total = 0

    for digit in str(number):
        total += (int(digit)) ** num_digits
    return number == total
