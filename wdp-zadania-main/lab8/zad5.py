def mySum(arr: list[int]) -> int:
    if len(arr) == 1:
        return arr[0]

    return arr[-1] + mySum(arr[0:len(arr)-1])


print(mySum([1, 2, 3, 4, 5]))
