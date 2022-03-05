matrix1 = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
]
matrix2 = [
    [8.0, 7.0, 5.0],
    [3.0, 4.0, 1.0]
]

result: list[list[float]] = []

for i in range(len(matrix1)):
    result.append([])

    for j in range(len(matrix1[i])):
        result[i].append(matrix1[i][j] + matrix2[i][j])

print(result)
