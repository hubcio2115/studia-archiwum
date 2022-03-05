psswd = input("Proszę podać hasło: ")
n = int(input("Proszę podać liczbę powtórzeń: "))

temp = ""

for i in range(n):
    while True:
        temp = input(f"Powtórz hasło {i+1}: ")

        if temp == psswd:
            break

print(f"Dziękuję podałeś prawidłowe hasło {n} razy.")
