from timeit import default_timer as timer


# time complexity: O(n * n + n)
def improvedFindBiggestRectangle(matrix: list[list[int]]) -> int:
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

    # Improved solution introduces stacks that remember heights and positions of certain rectangles
    # If one rectangle is a subrectangle of the other one it skips it
    maxArea = 0
    positionStack: list[int] = []
    heightStack: list[int] = []
    histogram.append(0)

    for i in range(len(histogram)):
        lastWidth = len(histogram) + 1

        while len(heightStack) != 0 and heightStack[-1] > histogram[i]:
            lastWidth = positionStack[-1]
            currentArea = (i - positionStack.pop()) * heightStack.pop()
            maxArea = max(currentArea, maxArea)

        if len(heightStack) == 0 or heightStack[-1] < histogram[i]:
            heightStack.append(histogram[i])
            positionStack.append(min(lastWidth, i))

    return maxArea


matrixes = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],  # 9.10000380827114e-06s
            [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],  # 1.550000160932541e-05s
            [],  # 1.2000018614344299e-06s
            [[1, 0, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1]]]  # 2.630000381032005e-05s


for matrix in matrixes:
    start = timer()
    improvedFindBiggestRectangle(matrix)
    stop = timer()
    Tn = stop - start
    print(f"{Tn}s")
