k = 10
m = 50

while True:
    if k != 0:
        if k < 5:
            k -= 1
            m += k
        else:
            k = k - 2
            m -= k
    else:
        print(f"k = {k}, m = {m}")
        break
