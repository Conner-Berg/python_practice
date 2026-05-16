"""Functions for calculating the number of grains of wheat on a chessboard.

A chessboard has 64 squares. Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time.
"""


def square(number):
    """Returns the number of grains on a given square of a chessboard.

    Args:
        number: The square number, must be between 1 and 64 inclusive.

    Returns:
        The number of grains on the given square (2 raised to the power of number - 1).

    Raises:
        ValueError: If number is not between 1 and 64.
    """

    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """Returns the total number of grains on a chessboard.

    Sums the grains across all 64 squares, where each square n
    holds 2^(n-1) grains.

    Returns:
        The total number of grains on the entire chessboard.
    """

    grains = 0
    for square_num in range(64):
        grains += 2**square_num
    return grains
