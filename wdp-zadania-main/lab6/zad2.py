matrix = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0]
]
k = 2

result: list[list[float]] = []

for i in range(len(matrix)):
    result.append([])

    for j in range(len(matrix[i])):
        result[i].append(matrix[i][j] * k)

print(result)
