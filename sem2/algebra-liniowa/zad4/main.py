from numpy import inf, seterr, isnan
from gssjrdn import gssjrdn
seterr(all="ignore")

if __name__ == "__main__":
    lines = open("./zad4/input.txt").read().splitlines()[5:]

    a = []
    b = []

    for line in lines:
        temp = []
        for string in line.split(" "):
            temp.append(float(string))

        a += [temp[:-1]]
        b += temp[-1:]

    [X, A] = gssjrdn(a, b)

    if inf in X or -inf in X:
        print("Układ ma nieskończenie wiele rozwiązań")

    for num in X:
        if isnan(num):
            print("Układ jest sprzeczny")
            exit()

    print("Układ ma jedno rozwiązanie: ")
    print("Wektor:")
    print(X)
    print()
    print("Macierz:")
    print(A)
