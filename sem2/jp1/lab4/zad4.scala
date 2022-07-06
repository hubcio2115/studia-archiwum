package lab4

import scala.annotation.tailrec

def divide[A](arr: List[A]): (List[A], List[A]) = {
  @tailrec
  def helper(arr: List[A], index: Int = 0, acc: (List[A], List[A]) = (Nil, Nil)): (List[A], List[A]) = arr match {
    case Nil => acc
    case head :: tail if index % 2 == 0 => helper(tail, index + 1, (acc(0) :+ head, acc(1)))
    case head :: tail => helper(tail, index + 1, (acc(0), acc(1) :+ head))
  }

  helper(arr)
}

@main
def lab4zad4(): Unit = {
  println(divide(List(1, 3, 5, 6, 7)))
}