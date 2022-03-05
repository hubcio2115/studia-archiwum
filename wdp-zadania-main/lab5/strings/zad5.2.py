word = ""
while True:
    word = input("Proszę podać słowo: ")

    if len(word) != 6:
        print("Słowo musi mieć 6 znaków")
        continue
    break

print(f"{word[-2]}, {word[-5:-2]}")
