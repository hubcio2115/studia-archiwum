def binomialTheorem(n: int, k: int) -> float:
    if k == 0 or k == n:
        return 1

    return binomialTheorem(n - 1, k - 1) + binomialTheorem(n - 1, k)


print(binomialTheorem(int(input()), int(input())))
