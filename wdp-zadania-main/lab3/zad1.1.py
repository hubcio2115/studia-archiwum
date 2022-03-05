k = int(input("Proszę wprowadzić wartość zmiennej k: "))
m = int(input("Proszę wprowadzić wartość zmiennej m: "))

while k != 0:
    if k < 5:
        k -= 1
        m += k
    else:
        k -= 2
        m -= k

print(m)
