package lab4

import scala.annotation.tailrec

def delete[T](arr: List[T], element: T): List[T] = {
  @tailrec
  def helper(arr: List[T], element: T, acc: List[T] = Nil): List[T] = arr match {
    case Nil => acc
    case head :: tail if head != element => helper(tail, element, acc :+ head)
    case _ :: tail =>  helper(tail, element, acc)
  }

  helper(arr, element)
}

@main
def lab4zad3(): Unit = {
  println(delete(List(2, 1, 4, 1, 3, 3, 1, 2), 1))
}