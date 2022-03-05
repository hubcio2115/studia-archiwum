def sortByInsert(arr: list[int]):
    j = len(arr) - 1
    while j >= 0:
        p = arr[j]
        i = j + 1
        while i < len(arr) and p > arr[i]:
            arr[i - 1] = arr[i]
            i += 1
        arr[i - 1] = p
        j -= 1
    return arr


print(sortByInsert([8, 3, 12, 4, -5, 10, 9, 8]))
