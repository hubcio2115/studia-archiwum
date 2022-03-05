def isInDB(name: dict[str, str]):
    file = open("baza.txt")
    lines = file.readlines()

    result: list[list[str]] = []
    for line in lines:
        result.append(line.split(';'))

    for i in range(len(result)):
        result[i].pop()
        result[i].pop(0)

    for entry in result:
        if name["firstName"] in entry and name["lastName"] in entry:
            return True

    return False


print(isInDB({"firstName": "Hubert", "lastName": "Kowalski"}))
