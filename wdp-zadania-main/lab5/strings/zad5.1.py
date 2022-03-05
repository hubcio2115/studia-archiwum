word = ""
while True:
    word = input("Proszę podać słowo: ")

    if len(word) > 7:
        print("Słowo może mieć maksymalnie 6 znaków")
        continue
    break

print(f"{word[4]}, {word[1:4]}")
