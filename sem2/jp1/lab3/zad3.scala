package lab3

import scala.annotation.tailrec

def fib(n: Int): Int = {
  @tailrec
  def helper(n: Int, acc1: Int = 2, acc2: Int = 1): Int = {
    if (n == 0) return acc1

    helper(n - 1, acc2, acc1 + acc2)
  }

  helper(n)
}

@main
def lab3zad3(): Unit = {
  println(fib(5))
}
