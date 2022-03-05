k = int(input("Proszę wprowadzić wartość zmiennej k: "))
m = int(input("Proszę wprowadzić wartość zmiennej m: "))

while True:
    if k == 0:
        print(m)
        break
    if k < 5:
        k -= 1
        m += k
    else:
        k -= 2
        m += k
