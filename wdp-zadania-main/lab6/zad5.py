matrix = [
    [1.0, 2.0, 3.0],
    [16.0, 8.0],
    [-2.0, 4.0, 5.0],
    [5.0, -22.0]
]

result = matrix[0]

for arr in matrix:
    if sum(result) < sum(arr):
        result = arr

print(result)
