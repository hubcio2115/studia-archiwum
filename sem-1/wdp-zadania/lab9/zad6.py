def sortByChoice(arr: list[int]):
    for i in range(len(arr)):
        p = i
        for j in range(i + 1, len(arr)):
            if arr[p] < arr[j]:
                p = j

        arr[p], arr[i] = arr[i], arr[p]
    return arr


arr = [3, 8, 12, 4, -5, 10, 9]
print(sortByChoice(arr))
