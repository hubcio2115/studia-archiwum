arr: list[float] = [float(i) for i in range(11)]

result = 0
for i in range(0, len(arr) + 1, 2):
    result += arr[i]

print(result)
