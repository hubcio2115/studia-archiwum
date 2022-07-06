package lab6

def pairPosNeg(seq: Seq[Double]): (Seq[Double], Seq[Double]) = {
  val (seq1, _) = seq.partition(element => element > 0.0)
  val (seq2, _) = seq.partition(element => element < 0.0)

  (seq1, seq2)
}

@main
def lab6zad2(): Unit = {
  println(pairPosNeg(Seq(-2, -1, 0, 1, 2)))
}
