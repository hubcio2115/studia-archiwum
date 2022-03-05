n = int(input("Proszę podać liczbę: ")) + 1

for a in range(1, n):
    for b in range(1, n):
        for c in range(1, n):
            for d in range(1, n):
                for e in range(1, n):
                    print(f"{a}{b}{c}{d}{e}")
