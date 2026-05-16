"""This module determine if a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)

A scalene triangle has all sides of different lengths.

For a shape to be a triangle at all, all sides have to be of length > 0, and the sum of the lengths of any two sides must be greater than or equal to the length of the third side.
"""


def isTriangle(sides):
    """Determine if side values represent a triangle.

    Args:
        sides: A sequence of three numeric values representing the side lengths
            of a triangle.

    Returns:
        Passes if all sides are > 0, and the sum of any two sides is greater than or equal to the third side.
        False otherwise.
    """

    first, second, third = sides
    if first <= 0 or second <= 0 or third <= 0:
        return False
    if first + second < third or first + third < second or second + third < first:
        return False
    return True


def equilateral(sides):
    """Determine if a triangle is equilateral.

    Args:
        sides: A sequence of three numeric values representing the side lengths
            of a triangle.

    Returns:
        True if all three sides are equal, False otherwise.
    """

    if not isTriangle(sides):
        return False
    first, second, third = sides
    if first <= 0 or second <= 0 or third <= 0:
        return False
    return first == second == third


def isosceles(sides):
    """Determine if a triangle is isosceles.

    Args:
        sides: A sequence of three numeric values representing the side lengths
            of a triangle.

    Returns:
        True if at least two sides are equal, False otherwise.
    """

    if not isTriangle(sides):
        return False
    first, second, third = sides
    if first <= 0 or second <= 0 or third <= 0:
        return False
    return first == second or first == third or second == third


def scalene(sides):
    """Determine if a triangle is scalene.

    Args:
        sides: A sequence of three numeric values representing the side lengths
            of a triangle.

    Returns:
        True if all three sides are different lengths, False otherwise.
    """

    if not isTriangle(sides):
        return False
    first, second, third = sides
    if first <= 0 or second <= 0 or third <= 0:
        return False
    return first != second and first != third and second != third


print(isosceles([1, 1, 3]))
