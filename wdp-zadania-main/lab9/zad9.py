def euclid(num1: int, num2: int) -> int:
    if num2 > num1:
        return euclid(num2, num1)
    if num1 % num2 == 0:
        return num2
    return euclid(num2, num1 % num2)


print(euclid(21345, 1234152))
