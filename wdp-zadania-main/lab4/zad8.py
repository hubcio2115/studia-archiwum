n = int(input("Proszę podać liczbę: "))

x = 0
y = 1

for i in range(0, n):
    x, y = y, x+y

print(x)
