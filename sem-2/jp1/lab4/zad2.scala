package lab4

import scala.annotation.tailrec

def maximum(arr1: List[Double], arr2: List[Double]): List[Double] = {
  @tailrec
  def helper(arr1: List[Double], arr2: List[Double], acc: List[Double] = List()): List[Double] = (arr1, arr2) match {
    case (Nil, Nil) => acc
    case (Nil, List(_*)) => acc.appendedAll(arr2)
    case (List(_*), Nil) => acc.appendedAll(arr1)
    case (head1 :: tail1, head2 :: tail2) if head1 > head2 => helper(tail1, tail2, acc :+ head1)
    case (_ :: tail1, head2 :: tail2) => helper(tail1, tail2, acc :+ head2)
  }

  helper(arr1, arr2)
}

@main
def lab4zad2(): Unit = {
  println(maximum(List(2.0, -1.6, 3.2, 5.4, -8.4), List(3.3, -3.1, 3.2, -4.1, -0.4, 5.5)))
}
