package lab3

import scala.annotation.tailrec

def reverse(str: String): String = {
  @tailrec
  def helper(str: String, acc: String = ""): String = {
    if (str.isEmpty) return acc

    helper(str.tail, str.head + acc )
  }

  helper(str)
}

@main
def lab3zad1(): Unit = {
  println(reverse("penis"))
}
