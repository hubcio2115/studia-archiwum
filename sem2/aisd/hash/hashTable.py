def hashStringToInt(string: str, tableSize: int):
    myHash = 17

    for char in string:
        myHash = (13 * myHash * ord(char)) % tableSize

    return myHash


class HashTable:
    def __init__(self) -> None:
        self.table = [[] for _ in range(3)]
        self.numItems = 0
        self.loadFactor = self.numItems / len(self.table)

    def resize(self):
        newTable = [[] for _ in range(len(self.table) * 2)]

        for item in self.table:
            if item:
                for pair in item:
                    index = hashStringToInt(pair[0], len(newTable))
                    if newTable[index]:
                        newTable[index].append(pair)
                    else:
                        newTable[index] = [pair]

        self.table = newTable

    def setItem(self, key: str, value: str):
        self.numItems += 1
        self.loadFactor = self.numItems / len(self.table)

        if self.loadFactor > .8:
            print("resizing")
            self.resize()

        index = hashStringToInt(key, len(self.table))
        if self.table[index]:
            self.table[index].append([key, value])
        else:
            self.table[index] = [[key, value]]

    def getItem(self, key):
        index = hashStringToInt(key, len(self.table))
        temp = next(filter(lambda x: x[0] == key, self.table[index]), None)

        if type(temp) == "list":
            return temp[1]

        return temp


myTable = HashTable()
myTable.setItem("firstName", "bob")
myTable.setItem("lastName", "tim")
myTable.setItem("age", 5)
myTable.setItem("dob", "1/2/3")

print(myTable.table)
print(myTable.getItem("firstName"))
print(myTable.getItem("lastName"))
print(myTable.getItem("age"))
print(myTable.getItem("dop"))
