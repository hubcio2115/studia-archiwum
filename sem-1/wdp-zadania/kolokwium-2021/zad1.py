def countA(word: str) -> int:
    if len(word) == 0:
        return 0
    if word[0] == "a":
        return countA(word[1:]) + 1
    return countA(word[1:])


print(countA("Alamakota"))
