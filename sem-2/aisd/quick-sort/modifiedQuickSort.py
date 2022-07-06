def partition(arr: list[int], pivot: int, right: int) -> int:
    x = arr[right]
    i = pivot - 1
    for j in range(pivot, right + 1):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    if i < right:
        return i
    else:
        return i - 1


def bubbleSort(arr: list[int]):
    for _ in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]


def modifiedQuickSort(arr: list[int], pivot: int, right: int, c: int = 1):
    if pivot < right:
        if right - pivot + 1 < c:
            bubbleSort(arr[pivot: right])
        else:
            q = partition(arr, pivot, right)
            modifiedQuickSort(arr, pivot, q, c)
            modifiedQuickSort(arr, q + 1, right, c)
