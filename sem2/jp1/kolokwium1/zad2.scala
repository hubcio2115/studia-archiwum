import scala.annotation.tailrec

/*
  Używając rekurencji ogonowej zdefiniuj funkcję:

    def pairwiseTest[A](l: List[A])(pred: (A, A) => Boolean)

  która sprawdzi, czy predykat „pred" jest spełniony dla wszystkich par
  elementów listy „l” o indeksach (i, długość(l) - i), dla i = 0.. długość(l)/2.

  Przykładowo, dla listy List(1,2,3,4,3,2,1) oraz predykatu równości, sprowadzi
  się to do następującej serii weryfikacji równości:

    l(0) == l(6)
    l(1) == l(5)
    l(2) == l(4)
    l(3) == l(3)

  Ogólnie, seria taka będzie miała postać:

    pred(l(0), l(l.length-1)) == true
    pred(l(1), l(l.length-2)) == true
    pred(l(2), l(l.length-3)) == true
    ...
    pred(l(l.length/2), l(l.length - l.length/2 - 1)) == true

  W przypadku pustej listy funkcja powinna zwrócić true

  Uwaga: w rozwiązaniu nie używaj zmiennych, ani mechanizmów imperatywnych jak pętle.
  Nie używaj też kolekcji języka Scala.
*/

def pairwiseTest[A](arr: List[A])(pred: (A, A) => Boolean): Boolean = {
  @tailrec
  def helper(arr: List[A], acc: Boolean = true)(pred: (A, A) => Boolean): Boolean = arr match {
    case Nil => acc
    case head :: Nil => helper(Nil, pred(head, head))(pred)
    case first +: Nil :+ last => helper(Nil, pred(first, last))(pred)
    case first +: body :+ last => helper(body, pred(first, last))(pred)
  }

  helper(arr)(pred)
}

@main
def zad2(): Unit = {
  println(pairwiseTest(List(1, 2, 3, 4, 4, 3, 2, 1))(_ == _))
}

