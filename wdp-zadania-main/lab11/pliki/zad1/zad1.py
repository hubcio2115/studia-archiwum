file = open("./liczby.txt")

arr = list(map(int, file.readlines()[0].split()))

print(
    f"Największą liczbą w pliku jest {max(arr)}, a najmniejszą jest {min(arr)}.")

file.close()
