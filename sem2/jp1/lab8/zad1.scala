package lab8

def evaluateGuess(secret: List[Int], guess: List[Int]): (Int, Int) = {
  val black = secret.zip(guess).foldLeft(0)((acc, element) => {
    if (element(0) == element(1)) acc + 1
    else acc
  })

  val secretMap = secret.groupBy(number => number)
  val guessMap = guess.groupBy(number => number)

  val white = guessMap.map(element => {
    secretMap.getOrElse(element(0), List()).length.min(element(1).length)
  }).sum - black

  (black, white)
}

@main
def lab8zad1(): Unit = {
  val secret = List(1, 3, 2, 2, 4, 5)
  val guess = List(2, 1, 2, 4, 7, 2)

  println(evaluateGuess(secret, guess))
}
