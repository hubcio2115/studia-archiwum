def bubbleSort(arr: list[int]):
    j: int = len(arr) - 1

    while j >= 1:
        i = 0
        while i < j:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1
        j -= 1
    return arr


print(bubbleSort([8, 4, 6, 7]))
