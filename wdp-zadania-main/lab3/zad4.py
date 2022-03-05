# Napisz skrypt, który dla liczby n wyznaczy największą liczbę m taką, że: 1 + 2 + 3 +...+m <=n.

n = int(input("Proszę wprowadzić liczbę: "))
result = 0

for m in range(0, n):
    result += m

    if result > n:
        print(f"m = {m - 1}")
        break
