n = int(input("Proszę podać liczbę: "))
x = 1

for i in range(1, n+1):
    print((n-i) * " " + "*" * x)
    x += 2

print(int(x / 2 - 2) * " " + "|_|")
