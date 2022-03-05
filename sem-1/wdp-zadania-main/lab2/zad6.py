a = int(input("Wprowadź pierwszy współczynnik: "))
b = int(input("Wprowadź drugi współczynnik: "))

if a != 0:
    x = -b/a
    print(x)
else:
    print(f"Współczynnik a jest równy 0, funkcja nie ma miejsc zerowych.")
