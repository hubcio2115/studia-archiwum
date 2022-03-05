n = int(input("Proszę wprowadzić liczbę: "))

for i in range(1, n + 1):
    print(i * "*")

print("")

for i in range(n, 0, -1):
    print(i * "*")
