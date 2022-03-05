num1 = int(input("Proszę podać pierwszą liczbę: "))
num2 = int(input("Proszę podać drugą liczbę: "))
num3 = int(input("Proszę podać trzecią liczbę: "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num3:
    print(num2)
else:
    print(num3)
