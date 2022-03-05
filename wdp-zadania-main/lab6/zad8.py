matrix = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
]

result = 0

for i in range(len(matrix)):
    result += matrix[i][i]

for i in range(-len(matrix), 0):
    result += matrix[i][i]

if len(matrix) % 2 != 0:
    temp = matrix[int(len(matrix)/2)]
    result -= temp[int(len(temp)/2)]

print(result)
