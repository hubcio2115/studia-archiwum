package lab6

def isOrdered[A](seq: Seq[A])(leq:(A, A) => Boolean): Boolean = {
  seq.sliding(2, 1).toList.foldLeft(true)((acc, element) =>
    if (leq(element.head, element(1))) acc
    else false
  )
}

@main
def lab6zad5(): Unit = {
  println(isOrdered(Seq(1, 2, 2, 4))(_ < _))
  println(isOrdered(Seq(1, 2, 2, 4))(_ <= _))
}
