matrix = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
]

result: list[list[float]] = []

for arr in matrix:
    result.append(arr[::-1])

print(result)
