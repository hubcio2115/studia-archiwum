/*
Plik temepratury.txt zawiera w pierwszej kolumnie rok oraz w kolejnych dwunastu kolumnach
średnią temperaturę za każdy miesiąc w danym roku (kolejno: styczeń, luty, marzec itd.).
Dane dotyczące każdego roku rozdzielone są pojedynczymi spacjami.

Przykładowo:

    1779 -4.9 2.2 3.8 9.5 15.4 16.4 17.9 19.5 14.7 9.3 4.1 1.4
    1780 -5.1 -4.3 4.4 5.9 14.2 17.2 19.4 17.9 13.1 9.4 2.8 -4.6
    1781 -4.0 -1.9 1.5 9.1 13.8 19.2 20.1 22.8 16.2 6.0 4.0 -3.6

Zdefiniuj funkcję:

    def maxAvgTemps(data: List[String]): Set[(Int, Double)]

która wyznaczy maksymalną średnią temperaturę dla każdego miesiąca, zwracając zbiór par w formacie (miesiąc, temperatura):

    Set((1,3.5), (2,5.1), (3,7.4), (4,13.2), (5,18.2), (6,22.4), (7,23.5), (8,23.8), (9,16.8), (10,12.6), (11,7.6), (12,3.9))

Rozwiąż to zadanie używając metod oferowanych przez kolekcje. Nie używaj zmiennych, kolekcji
mutowalnych, "pętli" (while, for bez yield, foreach) oraz nie definiuj żadnej funkcji rekurencyjnej.

*/

//def maxAvgTemps(data: List[String]): Set[(Int, Double)] = {
//    ???
//}
//
//@main
//def main(): Unit = {
//    val data = io.Source
//        .fromResource("temperatury.txt")
//        .getLines()
//        .toList
//    //...
//
//}
