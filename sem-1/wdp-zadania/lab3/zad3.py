# Napisz skrypt, który będzie pobierał od użytkownika liczby dopóki nie zostanie podana
# wartość 0 (0 oznacza koniec pobierania). Następnie wyświetli ile z pośród podanych liczb
# jest dodatnich, a ile ujemnych.

resultNeg = 0
resultPos = 0

while True:
    temp = float(input("Proszę wprowadzić liczbę: "))

    if temp == 0:
        print(
            f"Liczba podanych liczb dodatnich to {resultPos}, a ujemnych to {resultNeg}.")
        break
    elif temp > 0:
        resultPos += 1
    elif temp < 0:
        resultNeg += 1
