import scala.annotation.tailrec

/*
    Wykorzystując rekurencję (wyłącznie ogonową) zdefiniuj funkcję:

        def countResults[A,B,C](l1: List[A], l2: List[B])(f: (A, B) => C): Set[(C, Int)]

    która zaaplikuje funkcję „f” do elementów l1(i), l2(i), gdzie 0 <= i < min(l1.length, l2.length)
    oraz zwróci zbiór składający się z par:

        (wynik funkcji f, liczba par dla których f zwróciła dany wynik).

    Przykładowo dla:

        countResults(List(1,2,3), List(4,5,4,6))(_+_) == Set((5,1), (7,2))

    ponieważ: 1+4 = 5, 2+5 = 7, 4+3 = 7, 6 pomijamy bo to „nadmiarowy” element w drugiej z list.

    W rozwiązaniu należy skorzystać z mechanizmu dopasowania do wzorca (pattern matching).
    Nie używaj zmiennych ani „pętli” (while, for bez yield, foreach).
*/

def countResults[A, B, C](arr1: List[A], arr2: List[B])(helper: (A, B) => C): Set[(C, Int)] = {
  @tailrec
  def recursion(arr1: List[A], arr2: List[B], acc: Map[C, Int] = Map())(helper: (A, B) => C): Set[(C, Int)] = (arr1, arr2) match {
    case (Nil, List(_)) => acc.toSet
    case (List(_), Nil) => acc.toSet
    case (head1 :: tail1, head2 :: tail2) if acc contains helper(head1, head2) =>
      val temp = helper(head1, head2)
      recursion(tail1, tail2, acc.updated(temp, acc(temp) + 1))(helper)
    case (head1 :: tail1, head2 :: tail2) =>
      val temp = helper(head1, head2)
      recursion(tail1, tail2, acc.updated(temp, 1))(helper)
  }

  recursion(arr1, arr2)(helper)
}

@main
def zad1(): Unit = {
  println(countResults(List(1, 2, 3), List(4, 5, 4, 6))(_ + _))
}
