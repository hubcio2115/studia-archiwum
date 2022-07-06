package lab6

def deStutter[A](seq: Seq[A]): Seq[A] = {
  seq.foldLeft(Seq(): Seq[A])((acc, element) =>
    if (acc.indexOf(element) == -1) acc :+ element
    else acc
  )
}

@main
def lab6zad3(): Unit = {
  println(deStutter(Seq(1, 1, 2, 4, 4, 4, 1, 3)))
}