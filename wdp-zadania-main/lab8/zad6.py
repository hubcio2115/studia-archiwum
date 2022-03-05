def myMax(arr: list[int], num: int) -> bool:
    if not arr:
        return True
    elif arr[0] > num:
        return False

    return myMax(arr[1:], num)


print(myMax([1, 2, 3, 4, 5], 4))
