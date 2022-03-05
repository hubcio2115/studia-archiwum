matrix = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
]

maxLength = len(matrix[0])
for arr in matrix:
    if maxLength < len(arr):
        maxLength = len(arr)


result: list[list[float]] = [[] for _ in range(maxLength)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        result[j].append(matrix[i][j])

print(result)
