from zad1 import bubbleSort


def binarySearch(arr: list[int], searchedInt: int):
    left = 1
    right = len(arr)
    while left < right:
        middle = (left + right) // 2
        if arr[middle] < searchedInt:
            left = middle + 1
        else:
            right = middle
    if arr[left] == searchedInt:
        return left
    return None


print(binarySearch(bubbleSort([8, 3, 12, 4, -5, 10, 9, 8]), 4))
