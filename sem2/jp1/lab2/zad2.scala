package lab2

import scala.annotation.tailrec

@tailrec
def gcd(a: Int, b: Int): Int = {
  if (b == 0) a
  else gcd(b, a % b)
}

@main
def lab2zad2(num1: Int, num2: Int): Unit = {
  println(gcd(num1, num2))
}
