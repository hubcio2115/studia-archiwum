print("Działania na liczbach zespolonych.")
print("Wybierz działanie dostępne z opcji niżej: ")
print("1. dodawanie")
print("2. odejmowanie")
print("3. mnożenie")

operation: str = input("(1, 2 lub 3): ")
nums: int = int(input(
    "Dla ilu liczb chcesz wykonać operację?: "))

result = 0

if operation == "3":
    result += 1

for i in range(nums):
    temp = complex(input(f"Wprowadź liczbę {i+1}: "))

    if operation == "1":
        result += temp
    elif operation == "2":
        result -= temp
    elif operation == "3":
        result *= temp

print(f"Wynik to: {result}")
