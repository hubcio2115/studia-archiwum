package lab5

import scala.annotation.tailrec

def applyForAll[A, B](arr: List[A])(func: A => B): List[B] = {
  @tailrec
  def helper(arr: List[A], acc: List[B] = Nil)(func: A => B): List[B] = arr match {
    case Nil => acc.reverse
    case head :: tail => helper(tail, func(head) :: acc)(func)
  }

  helper(arr)(func)
}

@main
def lab5zad4(): Unit = {
  println(applyForAll(List(1, 3, 5))(n => n + 3))
}
