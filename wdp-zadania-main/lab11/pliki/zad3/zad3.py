from random import randint

result: list[int] = []
while True:
    if len(result) != 6:
        num = randint(1, 49)
        if num not in result:
            result.append(num)
        else:
            continue
    else:
        break

open("lotto.txt", "w").write("")

file = open("lotto.txt", "a")
for num in result:
    file.write(f"{str(num)} ")
file.close()
