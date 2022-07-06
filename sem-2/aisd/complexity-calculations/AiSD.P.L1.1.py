import math
from timeit import default_timer as timer


def f1(n: int):
    s = 0
    for j in range(1, n):
        s = s + 1 / j
    return s


def f2(n: int) -> float:
    s = 0
    for j in range(1, n):
        for k in range(1, n):
            s = s + k / j
    return s


def f3(n: int) -> float:
    s = 0
    for j in range(1, n):
        for k in range(j, n):
            s = s + k / j
    return s


def f4(n: int):
    s = 0
    for j in range(1, n):
        k = 2
        while k <= n:
            s = s + k / j
            k = k * 2
    return s


def f5(n: int):
    s = 0
    k = 2
    while k <= n:
        s = s + 1 / k
        k = k * 2
    return s


for n in range(1000, 10000, 1000):
    start = timer()
    f5(n)
    stop = timer()
    Tn = stop - start
    Fn = math.log(n, 2)
    print(n, '\t', format(Tn, '.8f'), '\t', int(Fn / Tn))

# inne funkcje czasu:

# Fn=math.log(n,2)
# Fn=n
# Fn=100*n
# Fn=n*math.log(n,2)
# Fn=n*n

# Po dopasowaniu wyniki wyglądały następująco
# f1: n { 28742239, 29322073, 29375764, 29520295, 29483913, 28662466, 29298877, 28656682, 28761620 }
# f1: 100*n { 1803133846, 1937815500, 1914376328, 1941361185, 1872946782, 1920768307, 1863560732, 1934507256, 1936179229 }
# f2: n*n { 22729769, 30742390, 30931599, 30778086, 31057008, 30676410, 30790336, 30781584, 29255367 }
# f3: n*n { 59772266, 59538096, 61165560, 60015979, 60305689, 61032491, 61155012, 60976800, 61345443 }
# f4: n*math.log(n, 2) { 20056924, 20018171, 18800808, 19601643, 18241403, 18888295, 19312830, 19417123, 17860238 }
# f5: math.log(n, 2) { 5315084, 10523785, 13866442, 15108313, 14733468, 15066922, 16148090, 16370939, 15769158 }
