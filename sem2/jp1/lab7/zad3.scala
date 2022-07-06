package lab7

def position[A](arr: List[A], element: A): Option[Int] = {
  val helper = arr.indexOf(element)
  if helper >= 0 then Option(helper)
  else None
}

@main
def lab7zad3(): Unit = {
  val myList = List(2, 1, 1, 5)
  println(position(myList, 1))
  println(position(myList, 3))
}