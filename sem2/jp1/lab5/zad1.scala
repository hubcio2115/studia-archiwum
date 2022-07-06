package lab5

import scala.annotation.tailrec

def cleanUp[T](arr: List[T]): List[T] = {
  @tailrec
  def helper(arr: List[T], acc: List[T] = Nil): List[T] = arr match {
    case Nil => acc.reverse
    case head :: Nil => (head :: acc).reverse
    case first :: second :: tail if first == second => helper(second :: tail, acc)
    case first :: second :: tail => helper(second :: tail, first :: acc)
  }

  helper(arr)
}

@main
def lab5zad1(): Unit = {
  println(cleanUp(List(1, 1, 2, 4, 4, 4, 1, 3)))
}
