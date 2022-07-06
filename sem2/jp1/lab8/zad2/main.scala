package lab8.zad2
import lab8.zad2.Competitor

def getResults(competitors: List[Competitor]): List[Competitor] = {
  competitors
    .sortBy(competitor => competitor.getAverageCharmScore)
    .sortBy(competitor => competitor.getAverageCharmScore + competitor.getAverageCunningScore)
}

@main
def lab8zad2(): Unit = {
  val competitor1 = new Competitor("Jan Kowalski", List(15, 8, 6, 20), List(12, 20, 11, 5))
  val competitor2 = new Competitor("Zofia Wieniawa", List(10, 8, 3, 16), List(19, 11, 13, 5))
  val competitor3 = new Competitor("Przemysław Okoń", List(13, 14, 13, 15, 16), List(20, 18, 15))

  val competitorsList: List[Competitor] = List(competitor1, competitor2, competitor3)

  getResults(competitorsList).foreach(element => println(element.name))
}
