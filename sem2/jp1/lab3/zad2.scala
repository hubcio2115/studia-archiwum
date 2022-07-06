package lab3

import scala.annotation.tailrec

def isPrime(num: Int): Boolean = {
  @tailrec
  def helper(num: Int, divisor: Int = 2): Boolean = {
    if (num < 2 && num > -2) return false
    if (num == 2) return true
    if (num % divisor == 0) return false
    if (divisor * divisor > num) return true

    helper(num, divisor + 1)
  }

  helper(num)
}

@main
def lab3zad2(): Unit = {
  println(isPrime(-7))
}
