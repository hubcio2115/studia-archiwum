from random import randint

n = int(input())
z1 = int(input())
z2 = int(input())


def randomNumbers(n: int, z1: int, z2: int) -> list[int]:
    result: list[int] = []

    for _ in range(n):
        result.append(randint(z1, z2))

    return result


print(randomNumbers(n, z1, z2))
