from typing import Any


def myBadHash(key: str) -> int:
    result = 0
    for char in key:
        result += ord(char)

    return result


def myGoodHash(key: str) -> int:
    result = 7 * (ord(key[0])) + ord(key[1])

    for i in range(len(key) - 2):
        result = result * 7 + ord(key[i+2])

    return result


def findLongestRowInMatrix(matrix: list[list[Any]]) -> int:
    result = 0
    for row in matrix:
        if result < len(row):
            result = len(row)

    return result


def averageSizeOfNonEmptyRowInMatrix(matrix: list[list[Any]]) -> float:
    sizes: list[int] = []
    for row in matrix:
        if len(row) != 0:
            sizes.append(len(row))

    return sum(sizes) / len(sizes)
