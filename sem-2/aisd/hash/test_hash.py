import myHash

if __name__ == "__main__":
    testStrings = open("./3700.txt", "r").read().split("\n")

    w17, d17, s17 = [[] for _ in range(17)],  [[]
                                               for _ in range(17)],  [[] for _ in range(17)]
    w1031, d1031, s1031 = [[] for _ in range(1031)], [[] for _ in range(1031)], [
        [] for _ in range(1031)]
    w1024, d1024, s1024 = [[] for _ in range(1024)], [[] for _ in range(1024)], [
        [] for _ in range(1024)]

    for string in testStrings:
        w17[hash(string) % 17].append(string)
        d17[myHash.myGoodHash(string) % 17].append(string)
        s17[myHash.myBadHash(string) % 17].append(string)

    for string in testStrings:
        w1031[hash(string) % 1031].append(string)
        d1031[myHash.myGoodHash(string) % 1031].append(string)
        s1031[myHash.myBadHash(string) % 1031].append(string)

    for string in testStrings:
        w1024[hash(string) % 1024].append(string)
        d1024[myHash.myGoodHash(string) % 1024].append(string)
        s1024[myHash.myBadHash(string) % 1024].append(string)

    print("w17:")
    print(
        f"Liczba pustych list: {len(list(filter(lambda x: len(x) == 0, w17)))}")
    print(
        f"Maksymalna długość listy: {myHash.findLongestRowInMatrix(w17)}")
    print(
        f"Średnia długość niepustych list: {myHash.averageSizeOfNonEmptyRowInMatrix(w17)}")

    print()

    print("d17:")
    print(
        f"Liczba pustych list: {len(list(filter(lambda x: len(x) == 0, d17)))}")
    print(
        f"Maksymalna długość listy: {myHash.findLongestRowInMatrix(d17)}")
    print(
        f"Średnia długość niepustych list: {myHash.averageSizeOfNonEmptyRowInMatrix(d17)}")

    print()

    print("s17:")
    print(
        f"Liczba pustych list: {len(list(filter(lambda x: len(x) == 0, s17)))}")
    print(
        f"Maksymalna długość listy: {myHash.findLongestRowInMatrix(s17)}")
    print(
        f"Średnia długość niepustych list: {myHash.averageSizeOfNonEmptyRowInMatrix(s17)}")

    print("-" * 20)

    print("w1031:")
    print(
        f"Liczba pustych list: {len(list(filter(lambda x: len(x) == 0, w1031)))}")
    print(
        f"Maksymalna długość listy: {myHash.findLongestRowInMatrix(w1031)}")
    print(
        f"Średnia długość niepustych list: {myHash.averageSizeOfNonEmptyRowInMatrix(w1031)}")

    print()

    print("d1031:")
    print(
        f"Liczba pustych list: {len(list(filter(lambda x: len(x) == 0, d1031)))}")
    print(
        f"Maksymalna długość listy: {myHash.findLongestRowInMatrix(d1031)}")
    print(
        f"Średnia długość niepustych list: {myHash.averageSizeOfNonEmptyRowInMatrix(d1031)}")

    print()

    print("s1031:")
    print(
        f"Liczba pustych list: {len(list(filter(lambda x: len(x) == 0, s1031)))}")
    print(
        f"Maksymalna długość listy: {myHash.findLongestRowInMatrix(s1031)}")
    print(
        f"Średnia długość niepustych list: {myHash.averageSizeOfNonEmptyRowInMatrix(s1031)}")

    print("-" * 20)

    print("w1024:")
    print(
        f"Liczba pustych list: {len(list(filter(lambda x: len(x) == 0, w1024)))}")
    print(
        f"Maksymalna długość listy: {myHash.findLongestRowInMatrix(w1024)}")
    print(
        f"Średnia długość niepustych list: {myHash.averageSizeOfNonEmptyRowInMatrix(w1024)}")

    print()

    print("d1024:")
    print(
        f"Liczba pustych list: {len(list(filter(lambda x: len(x) == 0, d1024)))}")
    print(
        f"Maksymalna długość listy: {myHash.findLongestRowInMatrix(d1024)}")
    print(
        f"Średnia długość niepustych list: {myHash.averageSizeOfNonEmptyRowInMatrix(d1024)}")

    print()

    print("s1024:")
    print(
        f"Liczba pustych list: {len(list(filter(lambda x: len(x) == 0, s1024)))}")
    print(
        f"Maksymalna długość listy: {myHash.findLongestRowInMatrix(s1024)}")
    print(
        f"Średnia długość niepustych list: {myHash.averageSizeOfNonEmptyRowInMatrix(s1024)}")


# w17:
# Liczba pustych list: 0
# Maksymalna długość listy: 248
# Średnia długość niepustych list: 220.23529411764707

# d17:
# Liczba pustych list: 0
# Maksymalna długość listy: 249
# Średnia długość niepustych list: 220.23529411764707

# s17:
# Liczba pustych list: 0
# Maksymalna długość listy: 247
# Średnia długość niepustych list: 220.23529411764707
# --------------------
# w1031:
# Liczba pustych list: 26
# Maksymalna długość listy: 12
# Średnia długość niepustych list: 3.725373134328358

# d1031:
# Liczba pustych list: 29
# Maksymalna długość listy: 11
# Średnia długość niepustych list: 3.7365269461077846

# s1031:
# Liczba pustych list: 189
# Maksymalna długość listy: 19
# Średnia długość niepustych list: 4.446555819477434
# --------------------
# w1024:
# Liczba pustych list: 30
# Maksymalna długość listy: 11
# Średnia długość niepustych list: 3.766599597585513

# d1024:
# Liczba pustych list: 21
# Maksymalna długość listy: 12
# Średnia długość niepustych list: 3.7328015952143567

# s1024:
# Liczba pustych list: 180
# Maksymalna długość listy: 19
# Średnia długość niepustych list: 4.436018957345971


#! P.1
# Oba rozmiary dają bardzo zbliżone do siebie wyniki, trudno stwierdzić, który daje lepsze.

#! P.2
# Rodzaj funkcji wpływa w taki sposób, że lepsze funkcje haszujące produkują mniej pustych list
# oraz średnia długość niepustych list jest mniejsza.
