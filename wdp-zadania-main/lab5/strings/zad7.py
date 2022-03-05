word = input("Proszę wprowadzić słowo: ")
temp = word[::-1]

if word == temp:
    print("Słowo jest palindromem.")
else:
    print("Słowo nie jest palindromem")
