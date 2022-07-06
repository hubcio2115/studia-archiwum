import sys
from random import randint
from timeit import default_timer as timer

from quickSort import quickSort
from modifiedQuickSort import modifiedQuickSort

sys.setrecursionlimit(5000)

if __name__ == '__main__':
    helper = ["DANE LOSOWE", "DANE NIEKORZYSTNE"]

    for i in range(len(helper)):
        data = []
        if i == 0:
            data100 = list(range(10))
            data500 = list(range(500))
            data1000 = list(range(1000))
            data2500 = list(range(2500))

            data100.reverse()
            data500.reverse()
            data1000.reverse()
            data2500.reverse()

            data = [data100, data500, data1000, data2500]

        else:
            data100 = [randint(0, 100) for _ in range(10)]
            data500 = [randint(0, 500) for _ in range(500)]
            data1000 = [randint(0, 1000) for _ in range(1000)]
            data2500 = [randint(0, 2500) for _ in range(2500)]

            data = [data100, data500, data1000, data2500]

        print(helper[i])
        print(
            f"rozmiar tablicy N | {' ' * 6} quickSort {' ' * 7} | {' ' * 3} modifiedQuickSort {' ' * 3} |")
        for arr in data:
            length = len(arr)
            temp = arr[:]

            start1 = timer()
            quickSort(arr, 0, length - 1)
            stop1 = timer()

            start2 = timer()
            modifiedQuickSort(temp, 0, length - 1)
            stop2 = timer()

            print(f"{' ' * (10 - len(str(length)))} {length} {' ' * 5} | {stop1 - start1}s {' ' * (22 - len(str(stop1 - start1)))} | {stop2 - start2}s {' ' * (23 - len(str(stop2 - start2)))} |")

        print()
