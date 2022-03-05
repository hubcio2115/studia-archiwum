a = int(input("Proszę wprowadzić pierwszą liczbę: "))
b = int(input("Proszę wprowadzić drugą liczbę: "))
temp1, temp2 = a, b

while temp1 != temp2:
    if temp1 > temp2:
        temp1 -= temp2
    else:
        temp2 -= temp1
print(f"Największym wspólnym dzielnikiem dla {a} i {b} jest {temp1} ")
