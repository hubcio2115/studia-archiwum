def partition(arr: list[int], pivot: int, right: int):
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


def quickSort(arr: list[int], pivot: int, right: int):
    if pivot < right:
        q = partition(arr, pivot, right)
        quickSort(arr, pivot, q)
        quickSort(arr, q + 1, right)
