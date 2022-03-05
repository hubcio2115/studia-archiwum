a = int(input("Wprowadź pierwszy współczynnik: "))
b = int(input("Wprowadź drugi współczynnik: "))
c = int(input("Wprowadź trzeci współczynnik: "))

delta = b**2 - (4 * a * c)

if delta < 0:
    print("Funkcja nie ma miejsc zerowych")
elif delta == 0:
    print(f"Funkcja ma jedno miejsce kwadratowe równe {-b / 2 * a}")
else:
    x1 = (-b - (delta//2)) / 2 * a
    x2 = (-b + (delta//2)) / 2 * a
    print(
        "Funkcja ma dwa miejsca kwadratowe równe kolejno x1 = {x1}, x2 = {x2}"
    )
