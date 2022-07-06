package lab7

def sumOpts(seq: Seq[Option[Double]]): Option[Double] = {
  if seq.forall(x => x.isEmpty) then return None
  seq.reduce((acc, element) => {
    if element.isEmpty then acc
    else Option(acc.get + element.get)
  })
}

@main
def lab7zad2(): Unit = {
  val myList = List(Some(5.4), Some(-2.0), Some(1.0), None, Some(2.6))
  assert(sumOpts(myList).contains(7.0))
  assert(sumOpts(List()).isEmpty)
  assert(sumOpts(List(None, None)).isEmpty)
}