package lab2

def even(num: Int): Boolean = {
  if (num % 2 == 0) {
    return true
  }
  false
}

@main
def lab2zad1(num: Int): Unit = {
  println(even(num))
}
