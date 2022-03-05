n = int(input("Proszę wprowadzić liczbę mnożeń: "))

arr = [i for i in range(1, n+1)]

result: list[list[int]] = [[] for _ in range(len(arr))]

for i in range(len(arr)):
    for j in range(len(arr)):
        result[i].append(arr[i] * arr[j])

for arr in result:
    print(arr)
