package lab7
def swap[A](arr: List[A]): List[A] = {
  val groupedByPluralIndexes = arr.groupBy(element => arr.indexOf(element) % 2 == 0)

  val zippedPluralIndexes = groupedByPluralIndexes(false).map(List(_))
  val zippedSingularIndex = groupedByPluralIndexes(true).map(List(_))

  zippedPluralIndexes
    .zipAll(zippedSingularIndex, Nil, Nil)
    .flatMap(Function.tupled(_ ::: _))
}

@main
def lab7zad5(): Unit = {
  println(swap(List(1, 2, 3, 4, 5)))
}
