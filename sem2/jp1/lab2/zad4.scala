package lab2

import scala.annotation.tailrec

def findPrimes(num: Int): Unit = {
  if (num > 2) {
    @tailrec
    def loop(num: Int, acc: Int = 2): Boolean = {
      if (acc > num / 2) return false
      if (zad3.isPrime(acc) && zad3.isPrime(num - acc)) {
        println(s"$num = $acc + ${num - acc}")
        return true
      }

      loop(num, acc + 1)
    }

     if (!loop(num)) println("Liczby nie można przedstawić jako sumę dwóch liczb pierwszych.")
  } else println("Błędne dane wejściowe.")
}

@main
def lab2zad4(num: Int): Unit = {
  findPrimes(8)
}
