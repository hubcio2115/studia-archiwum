file = open("wiersz.txt")
lines = file.readlines()

counters = {
    "upper": 0,
    "lower": 0,
    "digit": 0,
    "whiteSpaces": 0,
    "other": 0
}

for line in lines:
    for i in range(len(line)):
        if line[i].isupper():
            counters["upper"] += 1
        elif line[i].islower():
            counters["lower"] += 1
        elif line[i].isnumeric():
            counters["digit"] += 1
        elif line[i].isspace():
            counters["whiteSpaces"] += 1
        elif line[i] == "\\" and line[i+1] == "n":
            counters["whiteSpaces"] += 1
            break
        else:
            counters["other"] += 1

print(counters)
