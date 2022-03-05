n = int(input("Proszę podać liczbę całkowitą: "))

if (n > 0 and n < 10) or (n < 0 and n > -10):
    print(f"Liczba {n} jest jednocyfrowa.")
elif (n > 10 and n > 100) or (n < -10 and n > -100):
    print(f"Liczba {n} jest dwucyfrowa.")
elif (n > 100 and n < 1000) or (n < -100 and n > -1000):
    print(f"Liczba {n} jest trzycyfrowa.")
else:
    print("Liczba znajduje się poza przedziałem.")
