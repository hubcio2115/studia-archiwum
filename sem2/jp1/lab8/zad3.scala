package lab8

def threeNumbers(num: Int): List[(Int, Int, Int)] = {
  for {
    c <- (1 to num).toList
    b <- 1 until c
    a <- 1 until b
    if c * c == a * a + b * b
  } yield (a, b, c)
}

@main
def lab8zad3(): Unit = {
  println(threeNumbers(20))
}
