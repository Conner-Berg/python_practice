"""this module determines what Bob will reply to someone when they say something to him or ask him a question.

Bob only ever answers one of five things.
"""


def response(hey_bob):
    """Determines what Bob will reply

    Args:
        hey_bob (str): What you say to Bob.

    Returns:
        bool: What Bob says to you.
    """
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.strip().endswith("?"):
        return "Sure."
    if not hey_bob.strip():
        return "Fine. Be that way!"
    return "Whatever."
