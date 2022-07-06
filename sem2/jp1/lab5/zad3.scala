package lab5

import scala.annotation.tailrec

def isOrdered[T](arr: List[T])(leq: (T, T) => Boolean): Boolean = {
  @tailrec
  def helper(arr: List[T])(leq: (T, T) => Boolean): Boolean = arr match {
    case Nil | List(_) => true
    case first :: second :: tail if leq(first, second) => helper(second :: tail)(leq)
    case _ => false
  }

  helper(arr)(leq)
}

@main
def lab5zad3(): Unit = {
  println(isOrdered(List(1, 2, 2, 4))(_ < _))
  println(isOrdered(List(1, 2, 2, 4))(_ <= _))
}