def createMatrix(str1: str, str2: str) -> list[list[int]]:
    result = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                result[i][j] = result[i - 1][j-1] + 1
            else:
                result[i][j] = max(result[i - 1][j], result[i][j - 1])

    return result


def lcs(str1: str, str2: str) -> str:
    matrix = createMatrix(str1, str2)

    def helper(str1, str2, matrix) -> str:
        if str1 == "" or str2 == "":
            return ""
        if str1[-1] == str2[-1]:
            return helper(str1[:-1], str2[:-1], matrix) + str1[-1]
        else:
            if matrix[len(str1) - 1][len(str2)] > matrix[len(str1)][len(str2) - 1]:
                return helper(str1[:-1], str2, matrix)
            else:
                return helper(str1, str2[:-1], matrix)

    return helper(str1, str2, matrix)
