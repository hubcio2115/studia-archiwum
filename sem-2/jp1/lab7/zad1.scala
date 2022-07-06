package lab7

def freq[A](seq: Seq[A]): Set[(A, Int)] = {
  seq
    .groupBy(current => current)
    .map(current => (current.head, current(1).length))
    .toSet
}

@main
def lab7zad1(): Unit = {
  println(freq(Seq('a','b','a','c','c','a')))
}