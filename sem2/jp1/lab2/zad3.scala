package lab2

import scala.annotation.tailrec

object zad3 {
  def isPrime(num: Int): Boolean = {
    @tailrec
    def helper(num: Int, divisor: Int = 2): Boolean = {
      assert(num >= 2)

      if (num <= 2) return if (num == 2) true
      else false
      if (num % divisor == 0) return false
      if (divisor * divisor > num) return true

      helper(num, divisor + 1)
    }

    helper(num)
  }
}

@main
def lab2zad3(num: Int): Unit = {
  println(zad3.isPrime(num))
}
