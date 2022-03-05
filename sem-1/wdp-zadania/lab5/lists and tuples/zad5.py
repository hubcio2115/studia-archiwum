arr = [i for i in range(26)]

minimal = arr[0]
maximal = arr[0]

for num in arr:
    if minimal > num:
        minimal = num

    if maximal < num:
        maximal = num

print(f"Najmniejszym wyrazem listy jest {minimal}, a największym {maximal}")
