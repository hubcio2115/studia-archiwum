def factorial(num: int) -> int:
    if num == 1:
        return num

    return num * factorial(num - 1)
