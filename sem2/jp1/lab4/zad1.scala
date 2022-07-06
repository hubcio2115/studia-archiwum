package lab4

import scala.annotation.tailrec

def sum(arr: List[Option[Double]]): Option[Double] = {
  @tailrec
  def helper(arr: List[Option[Double]], acc: Double = 0): Option[Double] = arr match {
    case List() => Some(acc)
    case head :: tail if head.getOrElse(0.0) > 0 => helper(tail, acc + head.get)
    case _ :: tail => helper(tail, acc)
  }

  helper(arr)
}

@main
def lab4zad1(): Unit = {
  println(sum(List(Some(2.0), Some(4.0), Some(-3.0), None, Some(-3.0), None, Some(1.0))))
}
