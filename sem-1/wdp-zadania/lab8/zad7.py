def toBinary(num: int) -> str:
    if num == 0:
        return "0"
    if num == 1:
        return "1"

    return toBinary(int(num / 2)) + str(num % 2)


print(toBinary(int(input())))
