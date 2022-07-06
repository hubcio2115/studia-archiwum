from typing import Any

from matplotlib.pyplot import table


def hashStringToInt(string: str, tableSize: int,  i: int = 0) -> int:
    return (hash(string) + i) % tableSize


class HashTable:
    def __init__(self, initialSize: int) -> None:
        self.table = [None for _ in range(initialSize)]
        self.numItems = 0
        self.loadFactor = self.numItems / len(self.table)

    def resize(self) -> None:
        newTable = HashTable(len(self.table) * 2)

        for item in self.table:
            newTable.setItem(item[1], item)

        self.table = newTable.table

    def setItem(self, key: str, value) -> None:
        self.numItems += 1
        self.loadFactor = self.numItems / len(self.table)

        if self.loadFactor > 1:
            self.resize()

        i = 0
        while True:
            index = hashStringToInt(key, len(self.table), i)

            if self.table[index] == None:
                self.table[index] = value
                break

            i += 1

    def simulateSetItem(self, key: str, value) -> int:
        i = 0
        counter = 0
        while True:
            index = hashStringToInt(key, len(self.table), i)

            if self.table[index] == None:
                break

            i += 1
            counter += 1

        return counter

    def getItem(self, key) -> Any:
        i = 0
        while True:
            index = hashStringToInt(key, len(self.table), i)

            if self.table[index] == None:
                return None
            elif self.table[index][1] == key:
                return self.table[index]

            i += 1
