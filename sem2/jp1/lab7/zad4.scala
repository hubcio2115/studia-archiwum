package lab7

def indices[A](arr: List[A], element: A): Set[Int] = {
  arr
    .zipWithIndex
    .filter(pair => pair._1 == element)
    .map(pair => pair._2)
    .toSet
}

@main
def lab7zad4(): Unit = {
  val myList = List(1, 2, 1, 1, 5)
  println(indices(myList, 1))
  println(indices(myList, 7))
}