from hashTable import HashTable

if __name__ == "__main__":
    # 278805 % 3 = 0
    # [W + OL]
    # rozmiary
    lengths = [1021]  # , 1024, 2039, 4093, 4096, 16381]

    file = open("./hash-table/nazwiskaASCII.txt").read().splitlines()

    surnames = []
    for entry in file:
        temp = entry.split(" ")
        surnames += [[int(temp[0]), temp[1]]]

    results = []
    for length in lengths:
        # 5%
        mTable5 = HashTable(length)
        testTable = [pair for pair in surnames[-10:]]

        for pair in surnames[:int(length * 0.05)]:
            mTable5.setItem(pair[1], pair)

        m5 = 0
        for pair in testTable:
            m5 += mTable5.simulateSetItem(pair[1], pair)

        m5 /= len(testTable)

        # 35%
        mTable35 = HashTable(length)
        testTable = [pair for pair in surnames[-10:]]

        for pair in surnames[:int(length * 0.35)]:
            mTable35.setItem(pair[1], pair)

        m35 = 0
        for pair in testTable:
            m35 += mTable35.simulateSetItem(pair[1], pair)

        m35 /= len(testTable)

        # 65%
        mTable65 = HashTable(length)

        for pair in surnames[:int(length * 0.65)]:
            mTable65.setItem(pair[1], pair)

        m65 = 0
        for pair in testTable:
            m65 += mTable65.simulateSetItem(pair[1], pair)

        m65 /= len(testTable)

        # 95%
        mTable95 = HashTable(length)

        for pair in surnames[:int(length * 0.95)]:
            mTable95.setItem(pair[1], pair)

        m95 = 0
        for pair in testTable:
            m95 += mTable95.simulateSetItem(pair[1], pair)

        m95 /= len(testTable)

        results.append([length, [m5, m35, m65, m95]])

    for result in results:
        print(
            f"średnia liczba prób wstawienia elementów wynosi: {result[1][0]} dla m: {result[0]}")
        print(
            f"średnia liczba prób wstawienia elementów wynosi: {result[1][1]} dla m: {result[0]}")
        print(
            f"średnia liczba prób wstawienia elementów wynosi: {result[1][2]} dla m: {result[0]}")
        print(
            f"średnia liczba prób wstawienia elementów wynosi: {result[1][3]} dla m: {result[0]}")

# średnia liczba prób wstawienia elementów wynosi: 337.2 dla m: 1021
# średnia liczba prób wstawienia elementów wynosi: 643.2 dla m: 1021
# średnia liczba prób wstawienia elementów wynosi: 949.2 dla m: 1021

# średnia liczba prób wstawienia elementów wynosi: 338.2 dla m: 1024
# średnia liczba prób wstawienia elementów wynosi: 645.2 dla m: 1024
# średnia liczba prób wstawienia elementów wynosi: 952.2 dla m: 1024

# średnia liczba prób wstawienia elementów wynosi: 693.2 dla m: 2039
# średnia liczba prób wstawienia elementów wynosi: 1305.2 dla m: 2039
# średnia liczba prób wstawienia elementów wynosi: 1917.2 dla m: 2039

# średnia liczba prób wstawienia elementów wynosi: 1412.2 dla m: 4093
# średnia liczba prób wstawienia elementów wynosi: 2640.2 dla m: 4093
# średnia liczba prób wstawienia elementów wynosi: 3868.2 dla m: 4093

# średnia liczba prób wstawienia elementów wynosi: 1413.2 dla m: 4096
# średnia liczba prób wstawienia elementów wynosi: 2642.2 dla m: 4096
# średnia liczba prób wstawienia elementów wynosi: 3871.2 dla m: 4096

# średnia liczba prób wstawienia elementów wynosi: 5713.2 dla m: 16381
# średnia liczba prób wstawienia elementów wynosi: 10627.2 dla m: 16381
# średnia liczba prób wstawienia elementów wynosi: 15541.2 dla m: 16381
