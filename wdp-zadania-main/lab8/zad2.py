def reverse(word: str) -> str:
    if len(word) == 1:
        return word

    return reverse(word[1:]) + word[0]


print(reverse(input()))
