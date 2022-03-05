word = input("Proszę podać słowo.")
vowels = ["a", "e", "i", "o", "u", "y"]

result = 0
for sign in word:
    if sign in vowels:
        result += 1

print(f"Słowo zawiera {result} samogłosek.")
