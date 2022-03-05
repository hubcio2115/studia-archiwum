import os
import math


def add(a, b) -> int:
    return math.floor(a + b)


def to_sentence(string: str) -> str:
    string = string.capitalize()

    if string.endswith("."):
        return string
    return f"{string}."
