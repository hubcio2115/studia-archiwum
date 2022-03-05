n = int(input("Proszę podać liczbę: "))
arr: list[int] = []

for i in range(n):
    arr.append(int(input("Proszę podać liczbę: ")))


print(sum(arr)/len(arr))
