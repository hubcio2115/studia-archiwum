n = int(input("Proszę podać liczbę: "))

arr: list[int] = []

for i in range(0, n, 4):
    arr.append(i)

print(arr)
