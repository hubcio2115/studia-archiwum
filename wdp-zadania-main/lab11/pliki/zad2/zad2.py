arr = [1, 2, 3, 4, 5]

even = open("parzyste.txt", "a")
odd = open("nieparzyste.txt", "a")

for num in arr:
    if num % 2 == 0:
        even.write(f"{str(num)} ")
    else:
        odd.write(f"{str(num)} ")

even.close()
odd.close()
