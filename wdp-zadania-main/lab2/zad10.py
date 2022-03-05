freezing = 0
cold = 5
warm = 20
hot = 25

temperature = int(input("Proszę wprowadzić temperaturę: "))

if temperature != None:
    if temperature < freezing:
        print("Jest bardzo zimno.")
    if temperature > hot:
        print("Jest gorąco na dworze.")
    else:
        if temperature < cold:
            print("Jest chłodno.")
        elif temperature < warm:
            print("Jest neutralnie.")
        elif temperature < hot:
            print("Jest ciepło na dworze.")
else:
    print("Podano złą wartość.")
