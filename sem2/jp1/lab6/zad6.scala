package lab6

def freqMax[A](arr: List[A]) = {
    val uniques = arr.toSet
    val uniquesWithCounters = uniques.map(element => (element, arr.count(num => num == element)))
    val max = uniquesWithCounters.maxBy((_, howMuch) => howMuch).toList(1)

  (uniquesWithCounters.filter((_, counter) => counter == max).map((number, _) => number), max)
}

@main
def lab6zad6(): Unit = {
  println(freqMax(List(1, 1, 2, 4, 4, 3, 4, 1, 3)))
}
