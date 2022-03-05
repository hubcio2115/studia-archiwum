insc = input("Proszę wprowadzić napis: ")


def isAlpha(insc: str) -> bool:
    alphabet = ["a", "b", "c", "d", "e", "f", "h", "i", "j", "k", "l",
                "m", "n", "o", "u", "p", "r", "s", "t", "u", "w", "x", "y", "z"]

    for sign in insc:
        if sign not in alphabet:
            return False
    return True


print(isAlpha(insc))
