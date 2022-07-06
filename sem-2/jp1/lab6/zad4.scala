package lab6

def remElems[A](seq: Seq[A], k: Int): Seq[A] = {
  seq.zipWithIndex.filter(element => element(1) != k).map(element => element(0))
}

@main
def lab6zad4(): Unit = {
  println(remElems(Seq(1, 2, 3, 4, 5), 0))
}
