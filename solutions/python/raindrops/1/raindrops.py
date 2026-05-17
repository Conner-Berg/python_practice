"""This module converts a number into its corresponding raindrop sounds.

If a given number:

is divisible by 3, add "Pling" to the result.
is divisible by 5, add "Plang" to the result.
is divisible by 7, add "Plong" to the result.
is not divisible by 3, 5, or 7, the result should be the number as a string.
"""


def convert(number):
    """Determines what sound effect string is returned based on a given number.

    Args:
        number (int/float): Number to be divided for return string.

    Returns:
        str: Sound effect based on division, or the given arg.
    """

    raindrop_sound = ""

    if number % 3 == 0:
        raindrop_sound += "Pling"
    if number % 5 == 0:
        raindrop_sound += "Plang"
    if number % 7 == 0:
        raindrop_sound += "Plong"
    if raindrop_sound == "":
        raindrop_sound += str(number)

    return raindrop_sound
