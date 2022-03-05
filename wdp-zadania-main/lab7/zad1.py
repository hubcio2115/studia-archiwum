a = int(input("Proszę podać mnożnik: "))
n = int(input("Proszę podać liczbę operacji: "))


def multiply(a: int, n: int) -> None:
    for i in range(1, n + 1):
        print(f"{i} * {a} = {i * a}")


multiply(a, n)
