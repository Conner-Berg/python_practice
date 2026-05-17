"""This module translates text from English to Pig Latin. The translation is defined using four rules, which look at the pattern of vowels and consonants at the beginning of a word. These rules look at each word's use of vowels and consonants:

vowels: the letters a, e, i, o, and u
consonants: the other 21 letters of the English alphabet
"""

VOWELS = ("a", "e", "i", "o", "u")
CONSONANTS = (
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "y",
    "z",
)


def translate_word(text):
    """Translates a single English word to Pig Latin.

    Args:
        text: A single lowercase English word with no spaces.

    Returns:
        The Pig Latin translation of the word.
    """

    if text.startswith("xr") or text.startswith("yt") or text.startswith(VOWELS):
        return text + "ay"
    if "qu" in text:
        qu_index = text.index("qu")
        if all(letter in CONSONANTS for letter in text[:qu_index]):
            return text[qu_index + 2 :] + text[: qu_index + 2] + "ay"
    for index, letter in enumerate(text):
        if (letter in VOWELS or letter == "y") and index != 0:
            first_vowel = index
            part_1 = text[first_vowel:]
            part_2 = text[:first_vowel]
            return part_1 + part_2 + "ay"
    return text


def translate(text):
    """Translates English text to Pig Latin, supporting multiple words.

    Args:
        text: A string of one or more space-separated English words.

    Returns:
        The Pig Latin translation of the input text.
    """

    words = text.split(" ")
    translated = [translate_word(word) for word in words]
    return " ".join(translated)
