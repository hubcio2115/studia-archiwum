# Napisz skrypt, który dla dowolnej liczby w systemie dwójkowym wyświetli jego odpowiednik
# w systemie dziesiątkowym. Wykonaj to zadania bez korzystania z wbudowanych funkcji
# przeliczających na inny system liczbowy.

binary = input(
    "Proszę o wprowadzenie wartości dodatniej liczby w systemie dwójkowym: ")
result = 0
power = len(binary)

for char in binary:
    power -= 1

    if int(char) == 1:
        result += 2 ** power

print(f"Jej odpowiednik w systemie dziesiętnym to: {result}")
