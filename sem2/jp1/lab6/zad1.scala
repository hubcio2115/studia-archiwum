package lab6

def subSeq[T](seq: Seq[T], begIdx: Int, endIdx: Int): Seq[T] = {
  seq.drop(begIdx).take(endIdx)
}

@main
def lab6zad1(): Unit = {
  println(subSeq(Seq(1, 2, 3, 4, 5), 2, 4))
}