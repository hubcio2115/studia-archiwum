# Napisz skrypt, który będzie pobierał od użytkownika liczby dopóki nie zostanie podanawartość 0
# (0 oznacza koniec pobierania). Następnie wyświetli sumę podanych wartości.
# Wejście:
# Zmienna liczba, przechowująca kolejne podane liczby.
# Wyjście:
# Na ekranie pojawia się suma podanych liczb.Warunki poprawności zadania:
# Po podaniu wszystkich liczb wyświetla się ich suma. Upewnij się,
# że prawidłowa wartośćpojawia się przy podaniu liczbujemnych, ułamkowych.

result = 0

while True:
    temp = float(input("Wprowadź liczbę: "))

    if temp == 0:
        print(result)
        break

    result += temp
