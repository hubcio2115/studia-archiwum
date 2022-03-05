signs = open("znaki.txt")
open("palindrom.txt", "w").write("")
palindrome = open("palindrom.txt", "a")

words = signs.readlines()[0].split()

result = 0
for word in words:
    if word == word[::-1]:
        result += 1
        palindrome.write(f"{word} ")

print(f"W pliku znajduje się liczba {result} palindromów.")
