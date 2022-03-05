# Sortowanie bąbelkowe nierosnące
arr = [5, 3, 2, 7, 5, 8]

j = 0
while j <= len(arr)+1:
    i = len(arr) - 2
    while i >= j:
        if arr[i] < arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
        i -= 1
    j += 1

print(arr)
