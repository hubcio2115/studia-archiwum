a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

arr = []

if a < b and a < c:
    if b < c:
        arr = [a, b, c]
    else:
        arr = [a, c, b]
elif b < c:
    if a < c:
        arr = [b, a, c]
    else:
        arr = [b, c, a]
else:
    if a < b:
        arr = [c, a, b]
    else:
        arr = [c, b, a]

print(arr)
