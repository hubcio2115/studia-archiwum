package zad4

/*
    Korzystając wyłącznie z mechanizmów kolekcji języka Scala znajdź kraj o najdłużej rosnącym wskaźniku LadderScore.
    Innymi słowy, korzystając z załączonych danych szukamy kraju, dla którego wskaźnik LadderScore najdłużej
    utrzymał „dobrą passę” (z roku na rok się zwiększał).

    Zwróć uwagę na to, że w danych mogą wystąpić „linie” z brakującymi danymi. Takie linie powinny zostać
    POMINIĘTE. Brakujące dane oznaczają, że w linii występują sekwencje postaci: ,,, przykładowo:

        Kosovo,2020,6.294,,0.792,,0.880,,0.910,0.726,0.201

    Linie takie, jako „niewiarygodne” należy pominąć (oczywiście nie zmieniając samego pliku danych)
    zanim program rozpocznie analizę.

    W rozwiązaniu nie wolno używać zmiennych, ani konstrukcji imperatywnych, takich jak pętle
*/

@main
def zad4(): Unit = {
  val results = io.Source
    .fromResource("./resources/world-happiness-report.csv")
    .getLines
    .map(line => line.split(',').toList)
    .toList

  val listOfObjects = results.slice(0, -1).foldLeft(Nil: List[CountryData])((acc, country) => {
    val List( countryName, year, ladderScore, logGDPPerCapita, socialSupport, healthyLifeExpectancyAtBirth, freedomToMakeLifeChoices, generosity, perceptionsOfCorruption, positiveAffect, negativeAffect ) = country
    acc.appended(CountryData(countryName, year, ladderScore, logGDPPerCapita, socialSupport, healthyLifeExpectancyAtBirth, freedomToMakeLifeChoices, generosity, perceptionsOfCorruption, positiveAffect, negativeAffect))
  })

  println(listOfObjects)
}
