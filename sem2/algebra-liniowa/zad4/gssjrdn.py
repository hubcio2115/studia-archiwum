from typing import Any, Tuple
import numpy as np


def gssjrdn(a: list[list[int]], b: list[int]) -> Tuple[list[Any], np.ndarray]:
    matrix = np.array(a, float)
    vector = np.array(b, float)
    length = len(b)

    for k in range(length):
        if np.fabs(matrix[k, k]) == 0:
            for i in range(k + 1, length):
                if np.fabs(matrix[i, k]) > np.fabs(matrix[k, k]):
                    for j in range(k, length):
                        matrix[k, j], matrix[i, j] = matrix[i, j], matrix[k, j]
                    vector[k], vector[i] = vector[i], vector[k]
                    break

        pivot = matrix[k, k]
        for j in range(k, length):
            matrix[k, j] /= pivot
        vector[k] /= pivot

        for i in range(length):
            if i == k or matrix[i, k] == 0:
                continue
            factor = matrix[i, k]
            for j in range(k, length):
                matrix[i, j] -= factor * matrix[k, j]
            vector[i] -= factor * vector[k]

    return np.ndarray.tolist(vector), matrix
