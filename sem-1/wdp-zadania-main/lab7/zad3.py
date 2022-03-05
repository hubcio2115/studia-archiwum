x = int(input("Podaj pierwszą cyfrę: "))
y = int(input("Podaj drugą cyfrę: "))
z = int(input("Podaj trzecią cyfrę: "))
arr = [x, y, z]


def minMax(arr: list[int]) -> tuple[int, int]: return min(arr), max(arr)


print(minMax(arr))
