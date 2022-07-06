def heapify(arr: list[int], heapSize: int, i: int):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < heapSize and arr[left] < arr[i]:
        largest = left
    if right < heapSize and arr[right] < arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, heapSize, largest)

    return arr


def buildHeap(arr: list[int]):
    heapSize = len(arr)
    indexOfTheLastFather = int((len(arr) - 2) / 2)

    for i in range(0, indexOfTheLastFather, 1):
        heapify(arr, heapSize, i)

    return arr


def heapSort(arr: list[int]):
    arr = buildHeap(arr)
    heapSize = len(arr)

    for _ in range(len(arr)-1, 0, -1):
        arr[0], arr[heapSize - 1] = arr[heapSize - 1], arr[0]
        heapSize -= 1
        heapify(arr, heapSize, 0)

    return arr


arr: list[int] = []
for line in open('./input.txt').readlines():
    arr.append(int(line.replace('\n', '')))

open('./output.txt', 'w').write('')
file = open('./output.txt', 'a')

for num in arr:
    file.write(f"{num}\n")
