arr = [i for i in range(8)]
tup = tuple(i for i in range(8))

arr.append(8)

arr.pop(7)

print(arr[4], tup[4])

print(arr[2:4], tup[2:4])
