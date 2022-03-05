def myNumSum(num: int) -> int:
    if len(str(num)) == 1:
        return num

    return myNumSum(int(str(num)[1:])) + int(str(num)[0])


print(myNumSum(int(input())))
