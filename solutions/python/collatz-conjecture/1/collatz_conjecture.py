"""Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.

The Collatz Conjecture rules are simple. Pick any positive integer.

If it's even, divide it by 2.
If it's odd, multiply it by 3 and add 1.
Then, repeat these steps, continuing indefinitely, until you reach 1.
"""


def steps(number):
    """Calculate the number of Collatz Conjecture steps to reach 1.

    Repeatedly applies the Collatz rules to the given number until reaching 1:
    divide by 2 if even, multiply by 3 and add 1 if odd.

    Args:
        number (int): A positive integer to start the sequence from.

    Returns:
        int: The number of steps required to reach 1.

    Raises:
        ValueError: If number is less than or equal to 0.

    Examples:
        >>> steps(1)
        0
        >>> steps(6)
        8
    """

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    collatz_steps = 0

    while not number == 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        collatz_steps += 1
    return collatz_steps
