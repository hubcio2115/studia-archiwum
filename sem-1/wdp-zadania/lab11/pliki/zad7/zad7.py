encrypted_message = open("./lab11/zad7/szyfr.txt", "r").readlines()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def decrypt(message: list[str], shift: int):
    decrypted_message = ""

    for i in range(len(encrypted_message)):
        for c in encrypted_message[i]:
            if c in alphabet:
                position = alphabet.index(c)
                new_position = (position + shift) % 26
                new_character = alphabet[new_position]
                decrypted_message += new_character
            else:
                decrypted_message += c

    print(decrypted_message)


decrypt(encrypted_message, 3)
