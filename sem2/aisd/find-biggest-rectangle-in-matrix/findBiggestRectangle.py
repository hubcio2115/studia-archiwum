from timeit import default_timer as timer


# time complexity: O(n * n + n * n)
def findBiggestRectangle(matrix: list[list[int]]) -> int:
    # Checks if matrix is empty
    if len(matrix) == 0:
        return 0

    # Initializes histogram
    histogram = [0 for _ in range(len(matrix[0]))]

    # Iterates for each row and creates histogram
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                histogram[j] += 1

    # Brute force calculations for the maxArea of the submatrix of all 1s
    # Iterates for each possible rectangle in the histogram
    maxArea = 0

    for i in range(len(histogram)):
        minHeight = histogram[i]
        for j in range(i, len(histogram)):
            minHeight = min(minHeight, histogram[j])
            currentArea = (j - i + 1) * minHeight
            maxArea = max(currentArea, maxArea)

    return maxArea


matrixes = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],  # 1.340000017080456e-05s
            [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],  # 1.6199999663513154e-05s
            [],  # 1.400003384333104e-06s
            [[1, 0, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1]]]  # 3.420000575715676e-05s


for matrix in matrixes:
    start = timer()
    findBiggestRectangle(matrix)
    stop = timer()
    Tn = stop - start
    print(f"{Tn}s")
