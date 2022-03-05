hexNums = open("./szesnastkowo.txt").readlines()

hex_to_dec_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                    '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

hex_to_octal_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                      '7': 7, '8': 10, '9': 11, 'A': 12, 'B': 13, 'C': 14, 'D': 15, 'E': 16, 'F': 17}

for num in hexNums:
    num = num[:6]
    dec = 0
    octal = 0
    length = len(num) - 1

    for digit in num:
        # Wzory na przeliczanie hex na inne systemy liczbowe wziąłem ze StackOverflow
        dec += hex_to_dec_table[digit.upper()]*16**length
        octal += hex_to_octal_table[digit.upper()]*8**length
        length -= 1

    decimalOut = open("dziesietnie.txt", "a")
    decimalOut.write(f"{dec}\n")
    decimalOut.close()

    octalOut = open("osemkowo.txt", "a")
    octalOut.write(f"{octal}\n")
    octalOut.close()
