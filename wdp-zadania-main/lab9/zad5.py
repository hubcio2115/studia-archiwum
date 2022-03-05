def sortByChoice(arr: list[int]):
    for i in range(len(arr)):
        p = i
        for j in range(i + 1, len(arr)):
            if arr[p] > arr[j]:
                p = j

        arr[i], arr[p] = arr[p], arr[i]
    return arr


arr = [3, 8, 12, 4, -5, 10, 9]
print(sortByChoice(arr))
