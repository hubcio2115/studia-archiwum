package lab5

import scala.annotation.tailrec

def compress[T](arr: List[T]): List[(T, Int)] = {
  @tailrec
  def helper(arr: List[T], acc: List[(T, Int)] = Nil, str: String = ""): List[(T, Int)] = arr match {
    case Nil => acc.reverse
    case head :: tail =>
      tail match {
        case Nil => acc match {
          case accHead :: _ if head != accHead => helper(tail, (head, (str + head).length) :: acc)
          case _ => helper(tail, acc, str + head)
        }
        case h :: _ if head != h => helper(tail, (head, (str + head).length) :: acc)
        case _ => helper(tail, acc, str + head)
      }
  }

  helper(arr)
}

@main
def lab5zad2(): Unit = {
  println(compress(List('a', 'a', 'b', 'c', 'c', 'c', 'a', 'a', 'b', 'd')))
}