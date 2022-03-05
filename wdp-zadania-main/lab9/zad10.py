def sitoEratostenes(num: int, arr: list[int]):
    from math import sqrt

    for i in range(2, num):
        arr[i] = True
    for i in range(2, int(sqrt(num))):
        if arr[i]:
            k = 2
            j = i * k
            while j < num:
                arr[j] = False
                k += 1
                j = i * k
    for i in range(2, num):
        if arr[i]:
            print(i)


sitoEratostenes(10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
