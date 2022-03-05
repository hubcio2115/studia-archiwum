from zad1 import bubbleSort


def binarySearch(arr: list[int], left: int, right: int, num: int) -> int:
    if right >= left:

        middle = (right + left) // 2

        if arr[middle] == num:
            return middle

        elif arr[middle] > num:
            return binarySearch(arr, left, middle - 1, num)

        return binarySearch(arr, middle + 1, right, num)

    return -1


arr = [8, 3, 12, 4, -5, 10, 9, 8]
print(binarySearch(bubbleSort(arr), 0, len(arr) - 1, 4))
