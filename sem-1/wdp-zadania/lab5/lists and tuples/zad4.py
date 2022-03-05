n = int(input("Proszę podać długość tabel: "))

arr1 = [float(i) for i in range(n)]
arr2 = [float(i) for i in range(n, 0, -1)]

result = 0
for i in range(len(arr1)):
    result += arr1[i] * arr2[i]
print(result)
