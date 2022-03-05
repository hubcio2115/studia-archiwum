sentence = input("Proszę podać zdanie: ")

result = 0
for sign in sentence:
    if sign == " ":
        result += 1


print(f"Zdanie zawiera {result} słów.")
