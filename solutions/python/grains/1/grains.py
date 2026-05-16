def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    grains = 0
    for x in range(64):
        grains += 2**x
        x += 1
    return grains
