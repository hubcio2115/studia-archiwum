x = float(input("Podaj pierwszą cyfrę: "))
y = float(input("Podaj drugą cyfrę: "))
z = float(input("Podaj trzecią cyfrę: "))


def isPositive(num: float) -> bool:
    if num > 0:
        return True

    return False


def isTriangle(x: float, y: float, z: float) -> bool:
    if isPositive(x) and isPositive(y) and isPositive(z):
        if x < y + z:
            if y < x + z:
                if z < y + x:
                    return True

    return False


print(isTriangle(x, y, z))
