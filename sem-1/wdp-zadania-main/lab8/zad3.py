def fib(num: int) -> int:
    if num == 1:
        return num

    return fib(num - 1) + num


print(fib(10))
